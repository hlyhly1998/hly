
from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import init_config
from App.views import init_blue


def create_app(env_name=None):
    app = Flask(__name__)

    init_config(app, env_name)

    init_ext(app)

    init_api(app)

    init_blue(app)

    return app