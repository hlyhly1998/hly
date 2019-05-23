from flask_restful import Resource, fields, marshal_with, reqparse
import time
from App.models import Cinemas

parser = reqparse.RequestParser()
parser.add_argument('city', type=str, default='全部')
parser.add_argument('district', type=str)
parser.add_argument('sort', type=int, default=1)    # 1降序， -1正序
parser.add_argument('limit', type=int)


cinemas_fileds = {
    'name':fields.String,
    'city':fields.String,
    'district':fields.String,
    'address':fields.String,
    'phone':fields.String,
    'score':fields.Float,
    'hallnum':fields.Integer,
    'servicecharge':fields.Float,
    'astrict':fields.Integer,
    'flag':fields.Integer,
}

result_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'date': fields.String,
    'data': fields.List(fields.Nested(cinemas_fileds))
}


class CinemasResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        parse = parser.parse_args()
        city = parse.get('city')
        district = parse.get('district')
        sort = parse.get('sort')
        limit_num = parse.get('limit')

        cinemas = []
        if city == '全部':
            cinemas = Cinemas.query.all()
        else:
            cinemas = Cinemas.query.filter(Cinemas.city == city)

        if district:
            cinemas = cinemas.filter(Cinemas.district == district)

        if sort == 1:
            cinemas = cinemas.order_by(-Cinemas.score)
        elif sort == -1:
            cinemas = cinemas.order_by(Cinemas.score)

        if limit_num:
            cinemas = cinemas.limit(limit_num)

        response_data = {
            'status': 200,
            'msg': '获取影院信息成功',
            'date': str(time.ctime()),
            'data': cinemas
        }

        return response_data

