# call FLASK/.venv/Scripts/activate
# pip3 install -r FLASK/requirements.txt
# flask --app FLASK/application.py --debug run

from flask import Flask, request

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
    return "<div>"+username+"</div>"   #RESPUESTA