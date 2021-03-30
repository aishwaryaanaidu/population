from flask import request
import requests
from flask_restful import Resource
from bs4 import BeautifulSoup
import pandas as pd

class GetMapData(Resource):
    def get(self):
        try:
            url = "https://www.worldometers.info/world-population/population-by-country/"
            html = requests.get(url)
            soup = BeautifulSoup(html.text, "html.parser")
            # print(soup.prettify())
            table = soup.find("table", attrs={"id": "example2"})
            head = table.thead.find_all("tr")
            print(head)
            headings = []
            for th in head[0].find_all("th"):
                headings.append(th.text.replace("\n", "").strip())
            print(headings)
        except(ValueError, KeyError, TypeError) as exception:
            return {
                'message': 'Unexpected error {}'.format(exception)
            }, 400
        except Exception as exception:
            return {
                'message': 'Internal server error {}'.format(exception)
            }, 500
