from flask import Flask,request
import json
from login.dologin import do_the_login
from flask import render_template
from my_class.my_class import printclass


app = Flask(__name__,static_url_path='')
 
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/myclass')
def my_class():
    d='monday'
    username='admin'
    return render_template('my_class.html',day=d,my_list=printclass(d,username))

@app.route('/login')
def logins():
    return app.send_static_file('login.html')

@app.route('/dologin',methods=['POST'])
def dologin():
    data=request.get_data()
    print("data = %s" %data)
    username = request.form['user']
    password = request.form['pwd']
    print("username:"+username)
    print("password"+password)
    msg,statuscode = do_the_login(username,password)
    return msg,statuscode

if __name__ == '__main__':
    app.run(host='0.0.0.0')