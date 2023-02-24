import json
import re

import flask
from flask import Flask,request,jsonify,Response
import templates

app = Flask(__name__)


usuarios=[
    {"username":"carlos",
     "password":"123",
     "email":"cfrances@gmail.com",
     "dni":"48760807V",
     "isPremium":True,
     "id":0},
    {"username":"jose",
     "password":"123",
     "email":"jose@gmail.com",
     "dni":"48760807W",
     "isPremium":True,
     "id":1},
    {"username":"maria",
     "password":"123",
     "email":"maria@gmail.com",
     "dni":"48760807Y",
     "isPremium":True,
     "id":2},
    {"username":"juan",
     "password":"123",
     "email":"maria@gmail.com",
     "dni":"48760807Z",
     "isPremium":True,
     "id":3}
]


@app.route("/get-all-users")
def get_all_users():
    return usuarios

"""@app.route("/signup/",methods=["GET""POST"])
def hola():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

    return flask.render_template("login.html")"""

@app.route("/login")
def get_login():
    return flask.render_template("login.html")
@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data.decode('utf-8'))
    for user in usuarios:
        if user['username'] == data['username'] and user['password'] == data['password']:
            return "Login correcto"
    return Response('El usuario no existe', status=400)



@app.route("/get-user")
def get_user():
    args = request.args
    for user in usuarios:
        if user["id"] == args.get("id",0,type=int):
            return user

    return Response('Usuario no encontrado', status=400)

@app.route("/new-user",methods=["POST"])
def new_user():
    data = json.loads(request.data.decode('utf-8'))
    for user in usuarios:
        if data["username"] == user["username"] or not re.search("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", data["password"]) or \
                not re.search("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ",data["email"]) or re.search("^[0-9]{8,8}[A-Za-z]$",data["dni"]):
            return Response('Error al validadr los datos', status=400)
    return Response('Usuario creado correctamente', status=200)

if __name__ == '__main__':
    app.run(debug=True,port=5000)

