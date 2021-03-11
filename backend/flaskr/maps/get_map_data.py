from flask import request
import requests
from flask_restful import Resource
from bs4 import BeautifulSoup

class GetMapData(Resource):
    def get(self):
        try:
            page = requests.get("https://www.worldometers.info/world-population/population-by-country/")
            soup = BeautifulSoup(page.text, 'html.parser')
            # returns a list of tables present on the page. Choose the one you need
            table = soup.find_all('table')[0]
            for child in table.children:
                for td in child:
                    print(td)
        except (ValueError, KeyError, TypeError) as exception:
            return {
                'message': 'Unexpected'
            }, 400
        except Exception as exception:
            return {
                'message': 'Internal server error'
            }, 500
