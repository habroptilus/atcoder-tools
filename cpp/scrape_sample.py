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

lang = soup.find("span", class_="lang-ja")

if lang is None:
    result = soup.find_all("pre")
else:
    result = lang.find_all("pre")

if len(result) == 0:
    print("Error in Scraping.")
else:
    print("Create sample files...")
    for i in range(1, len(result)):
        content = result[i].string
        if (i - 1) % 2 == 0:
            filename = "input_{}_{}.txt".format(prob, (i - 1) // 2 + 1)
        else:
            filename = "answer_{}_{}.txt".format(prob, (i - 1) // 2 + 1)
        path_w = "{level_camel}/{level}{round:03d}/sample_{prob}/{filename}".format(
            level_camel=level.upper(), level=level, round=round, prob=prob, filename=filename)
        print(path_w)
        with open(path_w, mode='w') as f:
            f.write(content.lstrip())
    print("Complete!")
