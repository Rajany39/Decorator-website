import re
from flask import Flask,render_template,request,redirect,session
import os
from database import readimagebyid, readrecord

import pymysql
app = Flask(__name__)
app.secret_key=os.urandom(24)
conn = pymysql.connect(host='localhost',
                            database='onlinewebsite',
                            user='root',
                            password='')
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register')
def register(): 
    return render_template("register.html") 

@app.route('/home')     
def home():
    if 'id' in session:
        data=readrecord()
        return render_template("home2.html",data=data) 
    else:
        return redirect('/') 

@app.route('/login_validation',methods=['POST']) 
def login_validation():
    email=request.form.get("email")   
    password=request.form.get("password") 
    cursor.execute('''select * from `profile` Where `email` Like '{}' AND `password` Like '{}' '''
                    .format(email,password))
    users=cursor.fetchall()   
    if len(users)>0:
        
        
        session['id']=users[0][0]
        # session['name']=users[0][1]
        #session['email']=users[0][0][2]
        
       # session['email']=users['email']
        return redirect('/home')
    else:
        return redirect('/')

@app.route('/add_user',methods=['POST'])
def add_user():
    name=request.form.get("name")
    email=request.form.get("email")
    password=request.form.get("password") 
    cursor.execute('''Insert into `profile` (`id`,`name`,`email`,`password`)values
    (NULL,'{}','{}','{}')'''.format(name,email,password)  )
    conn.commit()
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')

@app.route('/cart/<id>')
def cart(id):
    data=readimagebyid(id)
    return render_template('cart.html',data=data)   


# @app.route('/update/<sid>')
# def update(sid):
#     data = searchrecord(sid)
#     #print(data)
#     return render_template('update.html',data=data)

if __name__ =="__main__":
    app.run(debug=True) 