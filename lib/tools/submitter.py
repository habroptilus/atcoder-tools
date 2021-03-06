"""指定したコードを提出する."""

import requests
from bs4 import BeautifulSoup
import logging as lg


class Submitter:

    BASE_URL = "https://atcoder.jp"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def submit(self, src_dir, level, rnd, prob, lang, extension, lang_id):
        """全て小文字"""
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

        submit_url = f"{self.BASE_URL}/contests/{level}{rnd:03d}/submit"

        html = session.get(submit_url)
        html.raise_for_status()
        soup = BeautifulSoup(html.text, 'lxml')

        csrf_token = soup.find(attrs={'name': 'csrf_token'}).get('value')
        task_screen_name = f"{level}{rnd:03d}_{prob}"

        source_code = self.load_source_code(
            src_dir, level, rnd, prob, lang, extension)

        submit_info = {
            "data.TaskScreenName": task_screen_name,
            "csrf_token": csrf_token,
            "data.LanguageId": lang_id,
            "sourceCode": source_code
        }

        result = session.post(submit_url, data=submit_info)
        result.raise_for_status()

        if result.status_code == 200:
            lg.info("Successfully Submitted!")
        else:
            raise Exception("Error in submitting...")

    def load_source_code(self, src_dir, level, rnd, prob, lang, extension):
        source_path = src_dir / \
            f"{level}/{rnd:03d}/{lang}/code_{prob}.{extension}"
        if source_path.exists():
            # 提出用ソースコードの読み込み
            with source_path.open("r") as f:
                source_code = f.read()  # ファイル終端まで全て読んだデータを返す
            f.close()
        else:
            raise Exception("File to submit is not found.")
        return source_code
