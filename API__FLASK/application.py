# para portatil, añadir FLASK/ antes de las rutas
# call .venv/Scripts/activate
# pip install -r requirements.txt
# flask --app application.py --debug run
# $env:FLASK_APP='application.py'

from flask import Flask, request
from flask_cors import CORS
from flask import render_template

application = Flask(__name__)
CORS(application)

#   PUERTO 5000
@application.route("/") #RUTA
def hello_world():
    print(request.method)
    return "<h1>Hello world</h1>"   #RESPUESTA

@application.post("/")
def hello_world_post():
    return "Hola desde post"

@application.route("/usuarios") #RUTA
def divMiNombre():
    return "<div>carlos</div>"   #RESPUESTA

@application.route("/usuarios/<username>") #RUTA
def return_username(username):
    return render_template("hello.html",username=username)  #RESPUESTA

@application.post("/create-todo")
def create_todo():
    data=request.data
    data=data.decode()
    print(data)
    return "ok"

@application.get("/get-todos")
def get_todos():
    data=[
        {
            "id":0,
            "todo":"mi primer todo",
            "completed":False
        },
        {
            "id":1,
            "todo":"mi segundo todo",
            "completed":False
        },
        {
            "id":2,
            "todo":"mi tercer todo",
            "completed":False
        },
    ]

    return data

@application.put("/complete-todo")
def complete_todo():
    pass

