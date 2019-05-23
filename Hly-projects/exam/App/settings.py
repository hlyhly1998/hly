import  os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class BaseConfig():
    DEBUG = False
    TESTING = False
    SECRET_KEY = '$%&$%YDYTRFXDCUFCYTFX'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'develop.db')


config = {
    'develop':DevelopConfig,
    'default':DevelopConfig,
}
def init_config(app, env_name):
    app.config.from_object(config.get(env_name or 'default'))










