# pylint: disable=missing-docstring

from concurrent.futures import ThreadPoolExecutor
import requests


class Requester:
    def get(self, url):
        response = requests.get(url, timeout=None).json()

        return response

    def executor(self, url_list):
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = executor.map(self.get, url_list)

        return list(results)
