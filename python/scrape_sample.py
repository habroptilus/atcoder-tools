"""Scrape sample cases in Atcoder."""

import requests
from bs4 import BeautifulSoup
import re
import sys
import config

"""
:param level: contest level(lower case)
:param round: number of round(ex 092)
:param prob: problem(a,b,c,d...)

:output_files: "ABC/abc092/sample/"直下にinputとanswerファイルを作成
"""

# パラメータセット
args = sys.argv
level = args[1]
round = int(args[2])
prob = args[3]
LOGIN_URL = "https://beta.atcoder.jp/login"

# セッション開始
session = requests.session()

# csrf_token取得
r = session.get(LOGIN_URL)
s = BeautifulSoup(r.text, 'lxml')

csrf_token = s.find(attrs={'name': 'csrf_token'}).get('value')


# ログイン
login_info = {
    "csrf_token": csrf_token,
    "username": config.USERNAME,
    "password": config.PASSWORD
}

result = session.post(LOGIN_URL, data=login_info)
result.raise_for_status()


target_url = "https://beta.atcoder.jp/contests/{level}{round:03d}/tasks/{level}{round:03d}_{prob}".format(
    level=level, round=round, prob=prob)

html = session.get(target_url)
html.raise_for_status()
soup = BeautifulSoup(html.text, 'lxml')

lang = soup.find("span", class_="lang-ja")

file_i = 0

if lang is None:
    result = soup.find_all("pre")
else:
    result = lang.find_all("pre")

if len(result) == 0:
    print("Error in Scraping.")
else:
    print("Create sample files...")

    for i in range(len(result)):
        content = result[i].string
        if content is None:
            continue

        if file_i % 2 == 0:
            filename = "input_{}_{}.txt".format(prob, file_i // 2 + 1)
        else:
            filename = "answer_{}_{}.txt".format(prob, file_i // 2 + 1)

        file_i += 1
        path_w = "{level_camel}/{level}{round:03d}/sample_{prob}/{filename}".format(
            level_camel=level.upper(), level=level, round=round, prob=prob, filename=filename)
        print(path_w)
        with open(path_w, mode='w') as f:
            f.write(content.lstrip())
    print("Complete!")
