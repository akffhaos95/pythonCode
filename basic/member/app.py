from flask import Flask, request, render_template, url_for, redirect, jsonify
import pymysql, os, cx_Oracle, pandas as pd, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "oracle://hr:hr@127.0.0.1:1521/xe"
app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:qwer1234@localhost/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    userid = db.Column(db.String(20), primary_key=True)
    userpw = db.Column(db.String(20))
    username = db.Column(db.String(20))
    userage = db.Column(db.Integer)
    usermail = db.Column(db.String(20))
    useradd = db.Column(db.String(50))
    usergender = db.Column(db.String(20))
    usertel = db.Column(db.String(20))

    def __repr__(self):
        return "userid %r  , username %r"%(self.userid, self,username)

    def __init__(self,userid, userpw, username, userage, usermail, useradd, usergender, usertel):
        self.userid = userid
        self.userpw = userpw
        self.username = username
        self.userage = userage
        self.usermail = usermail
        self.useradd = useradd
        self.usergender = usergender
        self.usertel = usertel
def dbDML(msg, req="Null", userid="Null"):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            if msg=="insert":
                data = makeList(msg, req)
                sql = 'insert into users values(%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(sql, data)
                connection.commit()
            elif msg=="update":
                data = makeList(msg, req)
                sql = '''
                    update users set 
                    userpw=%s, username=%s, userage=%s, 
                    usermail=%s, useradd=%s, usergender=%s, usertel=%s
                    WHERE userid = %s
                '''
                cursor.execute(sql, data)
                connection.commit()
            elif msg=="selectOne":
                sql = 'select * from users where userid=%s'
                cursor.execute(sql, userid)
                result = cursor.fetchone()
                return result
            elif msg=="selectList":
                sql = 'select * from users'
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
            elif msg=="delete":
                sql = 'delete from users WHERE userid = %s'
                cursor.execute(sql, userid)
                connection.commit()
    finally:
        connection.close()
def create_conn():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='qwer1234',
        db='test',
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
        )
    return connection
def makeList(msg, req):
    userid = req('userid')
    userpw = req('userpw')
    username = req('username')
    userage = req('userage')
    usermail = req('usermail')
    useradd = req('useradd')
    usergender = req('usergender')
    usertel = req('usertel')
    if msg=='update':
        return [userpw, username, userage, usermail, useradd, usergender, usertel, userid]
    elif msg=='insert':
        return [userid, userpw, username, userage, usermail, useradd, usergender, usertel]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usersform', methods=['POST', 'GET'])
def usersform():
    if request.method == 'GET':
        return render_template('usersform.html')
    else:
        req = request.form.get
        userid = req('userid')
        userpw = req('userpw')
        username = req('username')
        userage = req('userage')
        usermail = req('usermail')
        useradd = req('useradd')
        usergender = req('usergender')
        usertel = req('usertel')
        my_user = User(userid, userpw, username, userage, usermail, useradd, usergender, usertel)
        db.session.add(my_user)
        db.session.commit()
        #dbDML("insert", req=request.form.get) 
    return redirect('/list')

@app.route('/list')
def list():
    result = User.query.all()
    #result = dbDML("selectList")
    return render_template('list.html', list = result)

@app.route('/content/<userid>')
def content(userid):
    result = User.query.filter_by(userid=userid).one()
    #result = dbDML("selectOne", userid=userid)
    return render_template('content.html', list = result)

@app.route('/updateform/<userid>', methods=['POST','GET'])
def updateform(userid):
    if request.method == 'GET':
        result = User.query.filter_by(userid=userid).one()
        #result = dbDML("selectOne", userid=userid)
        return render_template('updateform.html', list=result)
    else:
        my_user = User.query.get(request.form.get('userid'))
        my_user.userid = request.form.get('userid')
        my_user.userpw = request.form.get('userpw')
        my_user.username = request.form.get('username')
        my_user.userage = request.form.get('userage')
        my_user.usermail = request.form.get('usermail')
        my_user.useradd = request.form.get('useradd')
        my_user.usergender = request.form.get('usergender')
        my_user.usertel = request.form.get('usertel')
        db.session.commit()
        #dbDML("update", req=request.form.get)
        return redirect('/list')

@app.route('/deleteform/<userid>')
def deleteform(userid):
    my_user = User.query.get(userid)
    db.session.delete(my_user)
    db.session.commit()
    #dbDML("delete",userid=userid)
    return redirect('/list')


@app.route('/ajaxlist', methods=['GET'])
def ajaxlist():
    result = User.query.all()
    #result = dbDML("selectList")
    return render_template('ajaxlist.html', list=result)

@app.route('/ajaxlist', methods=['POST'])
def ajaxlistpost():
    connection = create_conn()
    userid = request.form.get('userid')
    data = User.query.filter(User.userid.like('%'+userid+'%'))
    df = pd.read_sql(data.statement, data.session.bind)
    result = df.to_json(orient='records')
    # try:
    #     with connection.cursor() as cursor:
    #         sql="select * from users where userid like %s"
    #         userid='%'+userid+'%'
    #         cursor.execute(sql, userid)
    #         result = cursor.fetchall()
    #         print(result)
    # finally:
    #     connection.close()
    return result

@app.route('/imglist')
def imglist():
    print(os.path.dirname(__file__))
    dirname = os.path.dirname(__file__) + '/static/img/'
    filenames = os.listdir(dirname)
    return render_template('imglist.html', filenames=filenames)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
