import hashlib
import uuid

from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify

from App.ext import db
from App.models import User

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)


 # 发起重定向将用户名传给前端显示
@blue.route('/mv_name/')
def mv_name():
    token = session.get('token')
    if token:
        user = User.query.filter(User.token == token).first()
        return jsonify({'usertel':user.tel, 'status':'1'})
    else:

        return jsonify({'usertel':None, 'status':'-1'})

# 注册
@blue.route('/register/', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        tel = request.form.get('tel')
        password = request.form.get('password')

        user = User()
        user.tel = tel
        user.password = md5_password(password)
        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))

        db.session.add(user)
        db.session.commit()

        # 重定向
        session['token'] = user.token
        return redirect('/static/index/html/index.html')


    elif request.method == 'GET':
        return render_template('register.html')

def md5_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()



# 发起ajax请求
@blue.route('/check_tel/')
def check_tel():
    tel = request.args.get('tel')
    users = User.query.filter(User.tel==tel)
    if users.count()>0:
        user = users.first()

        return jsonify({'status':'-1','msg':'用户名已经被注册'})
    else:

        return jsonify({'status':'1', 'msg':'用户名可用'})



# 登录
@blue.route('/login/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        tel = request.form.get('tel')
        password = request.form.get('password')
        users = User.query.filter(User.tel==tel).filter(User.password==md5_password(password))
        if users.count()>0: # 存在
            user = users.first()

            user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))

            db.session.add(user)
            db.session.commit()

            session['token'] = user.token
            return redirect('/static/index/html/index.html')
        else: # 不存在
            error = '用户名或密码错误'
            return render_template('login.html', error=error)
    elif request.method == 'GET':

        return render_template('login.html')


# 退出
@blue.route('/quit/')
def quit():
    session.pop('token')
    return redirect('/static/index/html/index.html')