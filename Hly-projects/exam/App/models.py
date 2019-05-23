from App.ext import db


class Wheel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(256))


class Goods(db.Model):
    gid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    unit = db.Column(db.String(20))
    headImg = db.Column(db.String(256))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tel = db.Column(db.String(50))
    password = db.Column(db.String(256))
    token = db.Column(db.String(256))