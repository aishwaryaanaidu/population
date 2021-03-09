from flask import Blueprint
from flask_restful import Api

from flaskr.maps import get_map_data

maps = Blueprint('maps', __name__)
api = Api(maps)

api.add_resource(get_map_data.GetMapData, '/get_data')