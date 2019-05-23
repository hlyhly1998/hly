import random

from flask import request
from flask_restful import Resource

from App.ext import cache
from App.models import User


class SMSResource(Resource):
    def get(self):
        token = request.args.get('token')
        user = User.query.filter(User.token == token).first()


        #### 必备参数
        # 短信应用SDK AppID
        appid = 1400112809  # SDK AppID是1400开头

        # 短信应用SDK AppKey
        appkey = "8d8b808cb9073023631d241951f49fb4"

        # 需要发送短信的手机号码
        phone_numbers = [user.phone]
        print(phone_numbers[0])

        # 短信模板ID，需要在短信应用中申请
        template_id = 166915  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请

        # 签名
        sms_sign = "TPP短信验证"  # NOTE: 这里的签名"腾讯云"只是一个示例，真实的签名需要在短信控制台中申请，另外签名参数使用的是`签名内容`，而不是`签名ID`


        ##### 指定模板发送短信
        from qcloudsms_py import SmsSingleSender
        from qcloudsms_py.httpclient import HTTPError

        ssender = SmsSingleSender(appid, appkey)
        # 模板: 验证码、超时时间
        randomstr = random.randrange(100000,1000000)
        params = [randomstr, 3]  # 当模板没有参数时，`params = []`
        cache.set(user.token, randomstr, timeout=60*3)  # 验证码缓存 token:randomstr
        try:
            result = ssender.send_with_param(86, phone_numbers[0],
                                             template_id, params, sign=sms_sign, extend="",ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
        except HTTPError as e:
            print(e)
        except Exception as e:
            print(e)

        return {'msg':'发送验证码成功，请注意查收'}