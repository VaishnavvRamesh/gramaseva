from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import os

from database_operations import database_operations
from database_operations import database_operations

app = Flask(__name__)
db_obj = database_operations()


@app.route('/')
def dashboard_page():
    return render_template('front.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/user_login', methods=['POST','GET'])
def user_login():
    user_name=request.form['username']
    pwd=request.form['password']
    
    db_obj.connect_db()
    result = db_obj.validate_user(user_name,pwd)
    db_obj.conn.close()
    
    if result[0]:
        return render_template('home_page.html',name=result[1])
    else:
        return render_template('login.html',info=result[1])

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/user_signup', methods=['POST','GET'])
def user_signup():
    
    db_obj.connect_db()
    result = db_obj.is_user_exit(request.form)
    if(result[0]):
        return render_template('signup.html',info=result[1])
    
    res = db_obj.add_user(request.form)
    db_obj.conn.close()

    return render_template('signup.html',info=res)



if __name__ == '__main__':
    app.run(debug=True)