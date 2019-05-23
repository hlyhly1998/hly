from flask_restful import Api

from App.apis.ActiveApi import UserActive
from App.apis.AlipayApi import Pay, PayNotify, PayResult
from App.apis.CinemasApi import CinemasResource
from App.apis.CityApi import CityResource
from App.apis.HelloApi import Hello
from App.apis.IconApi import UserIcon
from App.apis.LoginApi import Login
from App.apis.MovieApi import MovieResource
from App.apis.PasswordApi import Password
from App.apis.RegisterApi import Register
from App.apis.SMSApi import SMSResource

api = Api()

def init_api(app):
    api.init_app(app)


# 添加资源
api.add_resource(Hello, '/hello/')

api.add_resource(CityResource, '/api/v1/citylist/') # 城市列表
api.add_resource(Register, '/api/v1/register/') # 注册
api.add_resource(UserActive, '/api/v1/active/') # 用户激活
api.add_resource(Login, '/api/v1/login/')   # 登录
api.add_resource(Password, '/api/v1/updatepd/') # 修改密码
api.add_resource(UserIcon, '/api/v1/usericon/') # 用户头像
api.add_resource(SMSResource, '/api/v1/sms/')   # 短信验证
api.add_resource(MovieResource, '/api/v1/movies/') #电影信息
api.add_resource(CinemasResource, '/api/v1/cinemas/') #影院信息

api.add_resource(Pay, '/api/v1/pay/')   # 支付
api.add_resource(PayNotify, '/api/v1/notify/')
# api.add_resource(PayResult, '/api/v1/result/')