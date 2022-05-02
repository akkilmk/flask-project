from flask import Blueprint,jsonify,session,Flask,escape,request,url_for,redirect

account = Blueprint("account",__name__)

import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akhilmk@125",
    database="flaskproject"
)

mycursor = mydb.cursor(dictionary=True)


@account.route('/',methods=['GET','POST'])
def login():
    username = escape(request.form['username'])
    password = escape(request.form['password'])
    
    mycursor.execute("SELECT * FROM user  WHERE username =%s and password=%s", [username,password])

    if mycursor is not None:
        session['username'] = username
        return redirect(url_for('account.home'))

    else:
        return 'not valid'



@account.route('/register',methods=['POST','GET'])
def register():

    id = escape(request.form['id'])
    username=escape(request.form['username'])
    password=escape(request.form['password'])

    sql = """ INSERT INTO user(id,username,password) 
    VALUES(%s,%s,%s)"""
    val = (id,username,password)
    mycursor.execute(sql,val)
    mydb.commit()

    return 'registration succesfully completed'



@account.route('/home')
def home():
    if 'username' in session:
        return "succesfully entired on home page"
    return "your are not authorized person"


@account.route('/logout')
def logout():
    session.pop('username', None)
    return "logout"