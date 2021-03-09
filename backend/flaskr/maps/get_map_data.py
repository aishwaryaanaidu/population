from flask import request
from flask_restful import Resource


class GetMapData(Resource):
    def get(self):
        return "Hello"