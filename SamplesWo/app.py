from flask import Flask

from SamplesWo.rest import storageroom
from SamplesWo.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(storageroom.blueprint)
    return app
