"""Scrape sample cases in Atcoder."""

import requests
from bs4 import BeautifulSoup
import re
import sys

"""
:param level: contest level(lower case)
:param round: number of round(ex 092)
:param prob: problem(a,b,c,d...)

:output_files: "ABC/abc092/sample/"直下にinputとanswerファイルを作成
"""

args = sys.argv
level = args[1]
round = int(args[2])
prob = args[3]
target_url = "https://beta.atcoder.jp/contests/{level}{round:03d}/tasks/{level}{round:03d}_{prob}".format(
    level=level, round=round, prob=prob)
r = requests.get(target_url)

soup = BeautifulSoup(r.text, 'lxml')
result = soup.find_all("pre")
for i in range(len(result) // 2):
    content = result[i + 1].string
    if content is None:
        continue

    if i % 2 == 0:
        filename = "input_{}_{}".format(prob, i // 2 + 1)
    else:
        filename = "answer_{}_{}".format(prob, i // 2 + 1)
    path_w = "{level_camel}/{level}{round:03d}/sample_{prob}/{filename}".format(
        level_camel=level.upper(), level=level, round=round, prob=prob, filename=filename)
    print(path_w)
    with open(path_w, mode='w') as f:
        f.write(content.strip())
