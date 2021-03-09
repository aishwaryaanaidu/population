from flask import Flask
from flaskr.maps import maps


def create_app(test_config=None):
    app = Flask(__name__)

    app.register_blueprint(maps, url_prefix='/maps')

    return app
