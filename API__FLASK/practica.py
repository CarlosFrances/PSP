from flask import Flask

application = Flask(__name__)

dict = {"username":"carlos","password":"frances","edad":24}

@application.route("/get-users") # endpoint + ruta nos sacará la edad
def get_users():
    edad=dict["edad"]

    return edad