from flask import request
from flask_restful import Resource


class GetMapData(Resource):
    def get(self):
        try:
            return "Hello"
        except (ValueError, KeyError, TypeError) as exception:
            return {
                'message': 'Unexpected'
            }, 400
        except Exception as exception:
            return {
                'message': 'Internal server error'
            }, 500
