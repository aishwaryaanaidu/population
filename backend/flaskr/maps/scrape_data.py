import requests
from flask_restful import Resource
from bs4 import BeautifulSoup
import re


class ScrapeData(Resource):
    @staticmethod
    def get_population_data():
        url = "https://www.worldometers.info/world-population/population-by-country/"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        # print(soup.prettify())
        table = soup.find("table", attrs={"id": "example2"})
        head = table.thead.find_all("tr")
        # print(head)
        headings = []
        for th in head[0].find_all("th"):
            value = th.text.replace("\n", "").strip()
            value = re.sub(r"\([^()]*\)", "", value)
            value = value.strip()
            value = value.replace(" ", "_")
            value = re.sub('[\W]', '', value)
            value = value.lower()
            headings.append(value)
        # print(headings)
        headings[0] = 'id'
        body = table.tbody.find_all("tr")
        # print(body)
        data = []
        for r in range(0, len(body)):
            row = []
            for td in body[r].find_all("td"):
                row.append(td.text.replace("\n", "").strip())
            data.append(row)
        map_data = []
        for array in data:
            temp_dictionary = {}
            for i in range(0, len(headings)):
                temp_dictionary[headings[i]] = array[i]
            map_data.append(temp_dictionary)
        return map_data
