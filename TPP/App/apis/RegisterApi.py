import uuid

from flask import render_template
from flask_mail import Message
from flask_restful import Resource, reqparse, fields, marshal_with
import time
from werkzeug.security import generate_password_hash

from App.ext import db, mail, cache
from  App.models import User

# 请求 格式定制
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='请提供用户名')
parser.add_argument('password', type=str, required=True, help='请提供密码')
parser.add_argument('email', type=str, required=True, help='请提供邮箱')
parser.add_argument('phone', type=str, required=True, help='请提供手机')


# 响应 格式定制
"""
{
    'status': 200,
    'msg':'注册成功',
    'error':'',
    'date': '2018xxxx',
    'data': {
        'username': 'atom',
        'permissions': 0,
        'icon': '/static/img/head.png/',
        'token': '%^&*()FGHJIOertyui12312312'
    }
}
"""
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


class Register(Resource):
    @marshal_with(result_fields)
    def post(self):
        # 获取用户信息
        parse = parser.parse_args()
        user = User()
        user.username = parse.get('username')
        user.password = generate_password_hash(parse.get('password'))
        user.email = parse.get('email')
        user.phone = parse.get('phone')
        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))

        # 返回数据
        response_data = {
            'status': 406,
            'msg': '注册失败',
            'date': str(time.ctime())
        }

        # 逻辑处理
        users = User.query.filter(User.username == user.username).filter(User.email == user.email)
        if users.count()>0: # 用户已存在
            response_data['error'] = '该用户已经注册过，请直接登录!'
            return response_data
        else:   # 用户不存在
            # 邮箱处理
            users = User.query.filter(User.email == user.email)
            if users.count()>0:   # 邮箱已被注册
                response_data['error'] = '邮箱已被注册'
                return response_data


            # 用户名处理
            users = User.query.filter(User.username == user.username)
            if users.count()>0:   # 用户名被占用
                response_data['error'] = '用户名被占用'
                return response_data


            # 存储数据库
            db.session.add(user)
            db.session.commit()

            # 写邮件
            active_url = 'http:///127.0.0.1:5000/api/v1/active?token=' + user.token
            username = user.username
            body_html = render_template('userActive.html', active_url=active_url, username=username)
            msg = Message(subject="激活邮件",  # 主题
                          html=body_html,    # 正文
                          sender="18924235915@163.com",  # 发件人
                          recipients=[user.email])  # 收件人
            # 发邮件
            mail.send(msg)

            # cahce操作
            # token:userid
            cache.set(user.token, user.id, timeout=30)

            # 返回数据
            response_data['status'] = 200
            response_data['msg'] = '注册成功'
            response_data['data'] = user

            return response_data

