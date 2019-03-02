"""Scrape sample cases in AtCoder."""

import requests
from bs4 import BeautifulSoup


class Scraper:
    BASE_URL = "https://atcoder.jp"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def scrape(self, level, round, prob):
        """
        :param level: contest level(ex abc)
        :param round: number of round(ex 92)
        :param prob: problem(a,b,c,d...)

        :output_files: [{"input": content,"answer": content},...]
        """

        # セッション開始
        session = requests.session()
        login_url = f"{self.BASE_URL}/login"
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

        target_url = f"{self.BASE_URL}/contests/{level}{round:03d}/tasks/{level}{round:03d}_{prob}"

        html = session.get(target_url)
        html.raise_for_status()
        soup = BeautifulSoup(html.text, 'lxml')

        lang = soup.find("span", class_="lang-ja")

        samples = []
        file_i = 0

        if lang is None:
            result = soup.find_all("pre")
        else:
            result = lang.find_all("pre")

        if len(result) == 0:
            print("Error in Scraping.")
        else:
            print("Create sample files...")
            sample = {}
            for i in range(len(result)):
                content = result[i].string
                if content is None:
                    continue

                content = content.replace("\r", "")
                content = content.lstrip()

                if file_i % 2 == 0:
                    sample["input"] = content
                else:
                    sample["answer"] = content
                file_i += 1
                if len(sample) == 2:
                    samples.append(sample)
                    sample = {}

        return samples
