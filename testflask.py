from flask import Flask,request
import json
from login.dologin import do_the_login
app = Flask(__name__,static_url_path='')
 
@app.route('/')
def hello_world():
    return 'Hello World!'

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
    return do_the_login(username,password)

if __name__ == '__main__':
    app.run(host='0.0.0.0')