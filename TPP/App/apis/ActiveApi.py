import uuid

from flask_restful import Resource, reqparse, fields, marshal_with

# 请求数据格式化
from App.ext import db, cache
from App.models import User
import time

parser = reqparse.RequestParser()
parser.add_argument('token', type=str, required=True, help='请携带token值')

# 响应数据格式化
class IconForm(fields.Raw):
    def format(self, value):
        return '/static/img/' + value

user_fields = {
    'username': fields.String,
    'permissions': fields.Integer,
    'icon': IconForm(attribute='icon'), # attribute='模型字段名'
    'token': fields.String
}

result_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'error':fields.String(default=''),
    'date': fields.String,
    'data': fields.Nested(user_fields, default='')
}

class UserActive(Resource):
    @marshal_with(result_fields)
    def get(self):
        # 获取token
        parse = parser.parse_args()
        token = parse.get('token')

        # 根据token获取userid
        userid = cache.get(token)
        if not userid:  # 不存在
            response_data = {
                'status': 401,
                'msg': '激活失败',
                'error': '激活超时，请联系管理员!',
                'date': str(time.ctime()),
            }
            return response_data

        # 删除token
        cache.delete(token)

        # 更改用户状态
        user = User.query.get(userid)
        user.isactive = True
        user.token = str(uuid.uuid5(uuid.uuid4(), 'active'))
        db.session.add(user)
        db.session.commit()

        response_data = {
            'status': 201,
            'msg': '激活成功',
            'date': str(time.ctime()),
            'data': user
        }

        return response_data