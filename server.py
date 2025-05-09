from flask import Flask, render_template, request, url_for, redirect, jsonify
import json
from database import *
app = Flask(__name__)
from flask import Flask, session

app = Flask(__name__)

# Set a secret key (should be random and unique)
app.secret_key = 'your_super_secret_key'
userdata = 0
@app.route("/bregister",methods=['POST','GET'])
def signup():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        status = Buyer_reg(username,email,password) 
        if status == 1:
            return render_template("blogin.html")
        else:
            return render_template("breg.html",m1="failed")        
    

@app.route("/blogin",methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        status = Buyer_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1: 
            session['username'] = request.form['username']                                     
            return render_template("index.html", m1="sucess")
        else:
            return render_template("blogin.html", m1="Login Failed")

@app.route('/')
def hello_world():
    return render_template('main.html')
@app.route('/bl')
def hello_world1():
    return render_template('blogin.html')
@app.route('/br')
def hello_world2():
    return render_template('breg.html')


@app.route('/new')
def new():
    print("Here we are")
    return render_template('result.html')
    # return jsonify(userdata)


@app.route('/getdata', methods=['GET'])
def getdata():
    print("here getedata")
    return jsonify(userdata)


@app.route('/result', methods=['GET', 'POST'])
def your_func():
    print(request.form)
    # print(type(request.form['data']))
    # print(json.loads(request.form))
    global userdata
    userdata = request.form
    # print(request.method)
    # print(request.form)
    # if (request.method == 'POST'):
    #     print("here I am")
    # return render_template('result.html')
    return redirect(url_for('new'))


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5500)
