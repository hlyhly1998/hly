import uuid

from flask_restful import Resource

from App.alipay import alipay

class Pay(Resource):    # 支付接口
    def post(self):
        # 获取token、orderid

        # 获取对应的订单号
        order_no = str(uuid.uuid5(uuid.uuid4(), 'orderid'))
        # 获取订单对应金额
        total = 9.9

        # 发起支付请求(对接支付宝)
        # def direct_pay(self, subject, out_trade_no, total_amount, return_url=None, **kwargs):
        # 返回签名后的支付参数
        url_args = alipay.direct_pay(
            subject='iPhonex - 9.9包邮',
            out_trade_no=order_no,
            total_amount=total,
            # return_url='http://112.74.55.3/api/v1/result/'
            return_url='http://112.74.55.3/about/'
        )

        re_url = 'https://openapi.alipaydev.com/gateway.do?{}'.format(url_args)

        return {'re_url':re_url}

class PayNotify(Resource):  # 支付宝 异步通知 【TPP服务器】
    def post(self):

        # 订单处理等操作
        # 根据订单号，找到对应的订单，并修改订单状态

        return {'msg':'success'}



class PayResult(Resource):  # 支付成功后 跳转的页面 【TPP客户端】
    def get(self):
        return {'msg':'支付成功，等待收货'}
