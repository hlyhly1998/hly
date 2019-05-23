from flask_restful import Resource, fields, marshal_with, marshal
from App.models import Letter,City


"""
# 响应格式化 定制
{
    'stauts':200,
    'msg':'获取数据成功',
    'data': {
        'A': [{},{},{}...],
        'B': [],
        'C': []
    }
}
"""
# city_fields = {
#     "cityCode" : fields.Integer,
#     "id" : fields.Integer,
#     "pinYin" :fields.String,
#     "regionName" : fields.String
# }
#
# letter_fields = {
#     'A': fields.List(fields.Nested(city_fields)),
#     'B': fields.List(fields.Nested(city_fields)),
#     'C': fields.List(fields.Nested(city_fields)),
#     'D': fields.List(fields.Nested(city_fields)),
#     'E': fields.List(fields.Nested(city_fields)),
# }
#
# result_fields = {
#     'stauts': fields.Integer,
#     'msg': fields.String,
#     'data': fields.Nested(letter_fields)
# }
#
# class CityResource(Resource):
#     @marshal_with(result_fields)
#     def get(self):
#         # 所有字母
#         letters = Letter.query.all()
#
#         # 具体数据
#         """
#         {
#             'A': [],
#             'B': []
#         }
#         """
#         data = {}
#
#         # 遍历所有字母
#         for letter in letters:
#             # letter.name >> 'A'
#             # letter.l_cities  >>  [{},{}]
#             data[letter.name] = letter.l_cities
#             # print(data)
#
#         response_data = {
#             'stauts': 200,
#             'msg': '城市列表获取成功',
#             'data': data
#         }
#
#         return response_data



city_fields = {
    "cityCode" : fields.Integer,
    "id" : fields.Integer,
    "pinYin" :fields.String,
    "regionName" : fields.String
}
# letter_fields = {
#     'A': fields.List(fields.Nested(city_fields)),
#     'B': fields.List(fields.Nested(city_fields)),
#     'C': fields.List(fields.Nested(city_fields)),
#     'D': fields.List(fields.Nested(city_fields)),
#     'E': fields.List(fields.Nested(city_fields)),
# }

# result_fields = {
#     'stauts': fields.Integer,
#     'msg': fields.String,
#     'data': fields.Nested(letter_fields)
# }

class CityResource(Resource):
    def get(self):
        # 所有字母
        letters = Letter.query.all()

        # 具体数据
        """
        {
            'A': [],
            'B': []
        }
        """
        # 具体数据列表
        data = {}
        # 数据的格式化

        letter_fields_dynamic = {}

        # 遍历所有字母
        for letter in letters:
            # letter.name >> 'A'
            # letter.l_cities  >>  [{},{}]
            data[letter.name] = letter.l_cities

            # 'A': fields.List(fields.Nested(city_fields)),
            letter_fields_dynamic[letter.name] = fields.List(fields.Nested(city_fields))


        # 动态生成 最终格式化
        result_fields = {
            'stauts': fields.Integer,
            'msg': fields.String,
            'data': fields.Nested(letter_fields_dynamic)
        }

        # 最终的数据
        response_data = {
            'stauts': 200,
            'msg': '城市列表获取成功',
            'data': data
        }

        # 根据对应格式 生成最终 需要的数据
        result = marshal(response_data, result_fields)

        return result