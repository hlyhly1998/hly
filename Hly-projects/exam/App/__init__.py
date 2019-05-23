from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import init_config
from App.views import init_blue


def create_app(env_name=None):
    app = Flask(__name__)

    # 配置 api
    init_api(app)

    # 配置 ext.py
    init_ext(app)

    # 配置settings.py
    init_config(app, env_name)

    # 配置 views.py
    init_blue(app)

    return app