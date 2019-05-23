from App.ext import db


# 字母模型类
class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 字母
    name = db.Column(db.String(8))
    # 声明关系
    l_cities = db.relationship('City', backref='letter', lazy=True)

# 城市模型类
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 城市编号
    cityCode = db.Column(db.Integer)
    # 拼音
    pinYin = db.Column(db.String(40))
    # 中文名
    regionName = db.Column(db.String(40))
    # 声明关系(属于哪个字母下)
    c_letter = db.Column(db.Integer, db.ForeignKey(Letter.id))


# 用户模型类
class User(db.Model):
    # 主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名
    username = db.Column(db.String(80), unique=True)
    # 密码
    password = db.Column(db.String(256))
    # 邮箱
    email = db.Column(db.String(40), unique=True)
    # 手机
    phone = db.Column(db.String(20))

    # 等级
    permissions = db.Column(db.Integer, default=0)
    # 头像
    icon = db.Column(db.String(80), default='head.png')
    # 用户状态
    isactive = db.Column(db.Integer, default=0)
    # 令牌
    token = db.Column(db.String(256))
    # 逻辑删除
    isdelete = db.Column(db.Boolean, default=False)


# 电影模型类
# insert into
# movies(id, showname, shownameen, director, leadingRole, type, country, language, duration, screeningmodel, openday, backgroundpicture, flag, isdelete)
# values(228830,"梭哈人生","The Drifting Red Balloon","郑来志","谭佑铭,施予斐,赵韩樱子,孟智超,李林轩","剧情,爱情,喜剧","中国大陆","汉语普通话",90,"4D",date("2018-01-30 00:00:00"),"i1/TB19_XCoLDH8KJjy1XcXXcpdXXa_.jpg",1,0);
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    showname = db.Column(db.String(256))
    shownameen = db.Column(db.String(256))
    director = db.Column(db.String(256))
    leadingRole = db.Column(db.String(256))
    type = db.Column(db.String(256))
    country = db.Column(db.String(100))
    language = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    screeningmodel = db.Column(db.String(20))
    openday = db.Column(db.Date)
    backgroundpicture = db.Column(db.String(256))
    flag = db.Column(db.Integer)    # 0全部，1热映，2即将上映
    isdelete = db.Column(db.Boolean)


# insert into
# cinemas(name,city,district,address,phone,score,hallnum,servicecharge,astrict,flag,isdelete) values("深圳戏院影城","深圳","罗湖","罗湖区新园路1号东门步行街西口","0755-82175808",9.7,9,1.2,20,1,0);
class Cinemas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256))
    city = db.Column(db.String(100))
    district = db.Column(db.String(100))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(40))
    score = db.Column(db.Float)
    hallnum = db.Column(db.Integer)
    servicecharge = db.Column(db.Float)
    astrict = db.Column(db.Integer)
    flag = db.Column(db.Integer)
    isdelete = db.Column(db.Integer)