## 一、前后端分离
- 服务端
```
- 轮播图模型
- 迁移生成表单
- 将轮播图数据插入到数据库
- 轮播图资源(API接口)
- 编写API文档
```

- 客户端(web)
```
- 添加页面(第三方引入)
- 基本页面结构(HTML)
- 基本样式(CSS)
- ajax获取数据(JS)
- DOM操作(渲染页面)
```

## 二、TPP项目 需求分析
- 首页
```
    影片信息
    影院信息
    区域选择
```

- 影片
```
    影片信息
```

- 影院
```
    影院信息
    生成订单
```

- 用户系统
```
    用户注册
    用户登录
    忘记密码
    修改信息
```

## 三、注册
- 字段
```
用户名
密码
邮箱
手机号
token
用户状态(是否激活)
用户权限(会员等级)
逻辑删除
头像
```

- 业务逻辑
```
# 激活接口永久生效(不符合实际)
1-调用注册接口(用户信息)
2-存入数据库(用户是未激活)
3-发送邮件(激活API + token)
4-点击邮件，调用激活接口(token)
5-根据token找到对应用户，将状态0改为1

# 激活接口是有时间限制的
1-调用注册接口(用户信息)
2-存入数据库(用户是未激活)
3-发送邮件(激活API + token)
4-超时处理(使用缓存token:userid)
5-点击邮件，调用激活接口(token)
6-根据token去缓存找userid
7-根据userid找到对应用户，将状态0改为1
```


## 四、flask-mail插件
- 文档
```
http://www.pythondoc.com/flask-mail/index.html
```

- 安装
```
pip install flask-mail
```

- 配置
```
MAIL_SERVER : 默认为 ‘localhost’
MAIL_USERNAME : 默认为 None
MAIL_PASSWORD : 默认为 None

mail = Mail(app)
```

- 使用
```
msg = Message("Hello",  # 发送内容
              sender="from@example.com",    # 发件人
              recipients=["to@example.com"])    # 收件人
```
