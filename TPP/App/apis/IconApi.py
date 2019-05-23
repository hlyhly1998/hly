import os

import werkzeug
from flask_restful import Resource, fields, marshal_with, reqparse

# 请求格式定制
from App.ext import db
from App.models import User
from App.settings import UPLOAD_DIR

parser = reqparse.RequestParser()
parser.add_argument('token', type=str, required=True, help='请输入token')
parser.add_argument('icon', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='请选择图片')

# 响应格式定制
result_fields = {
    'status':fields.Integer,
    'msg': fields.String,
    'error': fields.String,
    'data': fields.String(default='')   # 头像地址
}

class UserIcon(Resource):
    def post(self):
        parse = parser.parse_args()
        token = parse.get('token')

        response_data = {}

        users = User.query.filter(User.token == token)
        if users.count():   # 用户存在
            user = users.first()

            # 读取文件，保存文件
            imgfile = parse.get('icon')
            # 图片名
            fielname = '%d-%s' % (user.id, imgfile.filename)
            # 图片保存路径
            filepath = os.path.join(UPLOAD_DIR, fielname)
            # print(filepath)
            # 保存文件
            imgfile.save(filepath)

            # 更新数据库
            user.icon = fielname
            db.session.add(user)
            db.session.commit()

            response_data['status'] = 200
            response_data['msg'] = '文件上传成功'
            response_data['data'] = '/static/img/' + user.icon

            return response_data
        else:
            response_data['status'] = 401
            response_data['msg'] = '头像上传失败'
            response_data['error'] = '用户验证失败'
            return response_data