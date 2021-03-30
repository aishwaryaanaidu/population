from flaskr.maps.scrape_data import ScrapeData
from flask_restful import Resource


class GetMapData(Resource):
    def get(self):
        try:
            data = ScrapeData.get_scraped_data()
            return data
        except(ValueError, KeyError, TypeError) as exception:
            return {
                'message': 'Unexpected error {}'.format(exception)
            }, 400
        except Exception as exception:
            return {
                'message': 'Internal server error {}'.format(exception)
            }, 500
