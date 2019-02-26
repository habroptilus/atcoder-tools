"""Scrape sample cases in AtCoder."""

import requests
from bs4 import BeautifulSoup
import logging as lg
from pathlib import Path

"""
:param level: contest level(lower case)
:param round: number of round(ex 092)
:param prob: problem(a,b,c,d...)

:output_files: "ABC/abc092/sample/"直下にinputとanswerファイルを作成
"""


class Scraper:
    BASE_URL = Path("https://atcoder.jp")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def scrape(self, level, round, prob):
        # セッション開始
        session = requests.session()
        login_url = self.BASE_URL / "login"
        # csrf_token取得
        r = session.get(login_url)
        s = BeautifulSoup(r.text, 'lxml')

        csrf_token = s.find(attrs={'name': 'csrf_token'}).get('value')

        # ログイン
        login_info = {
            "csrf_token": csrf_token,
            "username": self.username,
            "password": self.password
        }

        result = session.post(login_url, data=login_info)
        result.raise_for_status()

        target_url = self.BASE_URL / \
            f"/contests/{level}{round:03d}/tasks/{level}{round:03d}_{prob}"

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
                save_path = f"{level}/{level}{round:03d}/sample_{prob}/{filename}"
                lg.info(save_path)
                with open(save_path, mode='w') as f:
                    f.write(content.lstrip())
            lg.info("Complete!")
