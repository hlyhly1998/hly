from flask_restful import Api

from App.apis.BannerApi import BannerResource
from App.apis.GoodsApi import GoodsResource
from App.apis.HelloApi import Hello

api = Api()

def init_api(app):
    api.init_app(app)

api.add_resource(Hello, '/hello/')
api.add_resource(BannerResource, '/banner/')
api.add_resource(GoodsResource, '/goods/')