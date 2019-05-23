from flask_restful import Resource, reqparse, marshal_with,  fields
from werkzeug.security import check_password_hash, generate_password_hash

from App.ext import db
from App.models import User

parser = reqparse.RequestParser()
parser.add_argument('token', type=str, required=True, help='请带入token')
parser.add_argument('oldpd', type=str, required=True, help='请带入旧密码')
parser.add_argument('newpd', type=str, required=True, help='请带入新密码')

result_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'error': fields.String(default='')
}

class Password(Resource):
    def post(self):
        # 获取数据
        parse = parser.parse_args()
        token = parse.get('token')
        oldpd = parse.get('oldpd')
        newpd = parse.get('newpd')

        user = User.query.filter(User.token == token).first()

        response_data = {}

        if check_password_hash(user.password, oldpd): # 验证通过
            user.password = generate_password_hash(newpd)
            db.session.add(user)
            db.session.commit()
            response_data['status'] = 200
            response_data['msg'] = '修改密码成功'
            return  response_data
        else:   # 旧密码错误
            response_data['status'] = 400
            response_data['msg'] = '修改密码错误'
            response_data['error'] = '旧密码输入错误'
            return response_data