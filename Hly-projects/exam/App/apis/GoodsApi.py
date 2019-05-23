from flask_restful import Resource, fields, marshal_with

from App.models import Goods

data = {
    'gid':fields.Integer,
    'name':fields.String,
    'price':fields.Integer,
    'unit':fields.String,
    'headImg':fields.String
}
response = {
    'status':fields.Integer,
    'msg':fields.String,
    'data':fields.List(fields.Nested(data))
}
class GoodsResource(Resource):
    @marshal_with(response)
    def get(self):
        goods = Goods.query.all()

        response_data = {
            'status':200,
            'msg':'获取数据成功',
            'data':goods
        }

        return response_data














