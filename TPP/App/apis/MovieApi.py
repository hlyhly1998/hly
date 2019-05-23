from flask_restful import Resource, reqparse, fields, marshal_with
import time
from App.models import Movies

parser = reqparse.RequestParser()
parser.add_argument('flag', type=int)

movie_fields = {
    'id': fields.Integer,
    'showname': fields.String,
    'shownameen': fields.String,
    'director': fields.String,
    'leadingRole': fields.String,
    'type': fields.String,
    'country': fields.String,
    'language': fields.String,
    'duration': fields.Integer,
    'screeningmodel': fields.String,
    'openday': fields.String,
    'backgroundpicture': fields.String,
    'flag': fields.Integer,
}

result_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'date': fields.String,
    'data': fields.List(fields.Nested(movie_fields))
}



class MovieResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        parse = parser.parse_args()
        flag = parse.get('flag') or 0 # 默认是所有

        if flag:
            movies = Movies.query.filter(Movies.flag == flag)
        else:
            movies = Movies.query.all()

        response_data = {
            'status': 200,
            'msg': '获取电影信息成功',
            'date': str(time.ctime()),
            'data': movies
        }

        return response_data