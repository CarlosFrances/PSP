# para portatil, añadir FLASK/ antes de las rutas
# call .venv/Scripts/activate
# pip install -r requirements.txt
# flask --app application.py --debug run
# $env:FLASK_APP='application.py'

from flask import Flask, request
from flask import render_template

application = Flask(__name__)

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

"""@application("/create-todo")
def create_todo():
    pass

@application("/get-todo")
def get_todo():
    pass"""