from flask_restful import Resource, fields, marshal_with

from App.models import Wheel

data = {
    'img':fields.String
}
response = {
    'status':fields.Integer,
    'msg':fields.String,
    'data':fields.List(fields.Nested(data))
}

class BannerResource(Resource):
    @marshal_with(response)
    def get(self):
        wheels = Wheel.query.all()

        response_data = {
            'status':200,
            'msg':'获取数据成功',
            'data':wheels
        }
        return response_data


