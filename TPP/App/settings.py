import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'static/img/')

class BaseConfig():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "$%^&*(3456789123f12gh3jdfq23423"

    # 邮箱
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = '18924235915@163.com'
    MAIL_PASSWORD = 'zyz123'    # 客户端授权密码

class DevelopConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/python1807tpp'


config = {
    'develop':DevelopConfig,
    'default':DevelopConfig,
}


def init_config(app, env_name):
    app.config.from_object(config.get(env_name or  'default'))