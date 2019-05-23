import uuid
from flask import render_template
from flask_mail import Message
from flask_restful import Resource, fields, reqparse, marshal_with
import time

# 请求数据格式
from werkzeug.security import check_password_hash

from App.ext import mail, cache, db
from App.models import User

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='请带入用户名')
parser.add_argument('password', type=str, required=True, help='请带入密码')


# 响应数据格式
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

class Login(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        username = parse.get('username')
        password = parse.get('password')

        response_data = {
            'status': 401,
            'msg': '登录失败',
            'date': str(time.ctime()),
        }

        users = User.query.filter(User.username == username)
        if users.count()>0: # 有对应的用户春存在
            # 获取用户
            user = users.first()

            # 密码验证
            if check_password_hash(user.password, password):   # 密码正确
                # 删除
                if user.isdelete == True:
                    response_data['error'] = '该用户已销户!'
                    return response_data

                # 未激活
                if user.isactive == False:
                    response_data['error'] = '用户未激活，激活邮件已经重新发送，请激活后登录'
                    # 写邮件
                    active_url = 'http:///127.0.0.1:5000/api/v1/active?token=' + user.token
                    username = user.username
                    body_html = render_template('userActive.html', active_url=active_url, username=username)
                    msg = Message(subject="激活邮件",  # 主题
                                  html=body_html,  # 正文
                                  sender="18924235915@163.com",  # 发件人
                                  recipients=[user.email])  # 收件人
                    # 发邮件
                    mail.send(msg)

                    # cahce操作
                    # token:userid
                    cache.set(user.token, user.id, timeout=30)

                    return response_data

                # 成功
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                db.session.add(user)
                db.session.commit()
                response_data['msg'] = '登录成功'
                response_data['status'] = 200
                response_data['data'] = user
                return response_data

            else:   # 密码错误
                response_data['error'] = '密码错误'
                return response_data
        else:   # 不存在
            response_data['error'] = '用户不存在'
            return  response_data