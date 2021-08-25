
from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect, url_for, send_from_directory, render_template
import json
import pyrebase

app = Flask(__name__)

# login으로 변경해야함
# config = {
#    "apiKey": "AIzaSyASyU5Qxe0zJZDVT1-oTYEVIcDYJzZNdA8",
#    "authDomain": "aitutor-894f0.firebaseapp.com",
#    "databaseURL": "https://aitutor-894f0-default-rtdb.firebaseio.com",
#    "projectId": "aitutor-894f0",
#    "storageBucket": "aitutor-894f0.appspot.com",
#    "messagingSenderId": "145018138005",
#    "appId": "1:145018138005:web:ea124ef3292ae2d0cb5a9c",
#    "measurementId": "G-0YF0B8C5EC"
# }
#
#
# # db settings
# firebase = pyrebase.initialize_app(config)
# db = firebase.database()
# db.child("member").child("124124124").child("test0").child("part1").push({
#        "similarity":94,"pronunciation" : 41,
#        "fluency" : 53,
#        "expression" : 64,
#        "relevance" : 72,
#        "url" : "alkjlskd1111"})


@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/post',methods=["POST"])
def hello_post():
    value = request.form['android_id']
    print(value)
    value2 = request.form['url']
    print(value2)

    return ('서버 통신 :' + value+','+value2)

@app.route('/one')
def hello_one():
    return "Hello one"


@app.route('/two')
def hello_two():
    return "Hello two"



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
