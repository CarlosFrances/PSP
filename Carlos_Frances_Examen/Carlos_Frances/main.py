from flask import Flask,jsonify
#from dateutil.parser import parse

#prueba para expresiones regulares
import re

app = Flask(__name__)

#lista de datos inicial para probar las rutas
listaUsuarios = {
    "Usuarios":[
        {
            "usuario":"carlos1",
            "contraseña":"abc",
            "nombre":"carlos",
            "correo":"carlos@carlos.com",
            "nacimiento":"19-11-1998"
        },
{
            "usuario":"juan1",
            "contraseña":"abcd",
            "nombre":"juan",
            "correo":"juan@juan.com",
            "nacimiento":"19-11-2000"
        },
{
            "usuario":"alejandro1",
            "contraseña":"abcde",
            "nombre":"alejandro",
            "correo":"alejandro@alejandro.com",
            "nacimiento":"19-11-2001"
        },
    ]

}


@app.route("/registrar/<usuario>/<password>/<nombre>/<correo>/<nacimiento>")
def registrar(usuario:str,password:str,nombre:str,correo:str,nacimiento:str):

    # regex de correo (no he conseguido que funcione)
    regexCorreo= re.compile('\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')

    # regex de fecha de nacimiento (no he conseguido que funcione)
    regexNacimiento=re.compile("\s+(?:0[1-9]|[12][0-9]|3[01])[--.](?:0[1-9]|1[012])[--.](?:19\d{2}|20[01][0-9]|2020)\b")

    # regex de prueba (si ha funcionado en la prueba)
    regexPrueba=re.compile("hola")


    # se retornará el usuario registrado en caso de que los parámetros sean aceptados por las condiciones y las expresiones regulares.
    # si no se cumplen dichas condiciones, retornará un error
    if isinstance(usuario,str) and isinstance(password,str) and isinstance(nombre,str) and regexCorreo.match(correo) and regexNacimiento.match(nacimiento):

        # creamos un objeto con los parámetros introducidos y lo devolvemos
        newUser = {
            "usuario":
                {
                    "usuario": usuario,
                    "contraseña": password,
                    "nombre": nombre,
                    "correo": correo,
                    "nacimiento": nacimiento
                }
        }

        return newUser

    else:
        return "Error: los datos introducidos no son válidos"


    # pruebas regex
    """if regexCorreo.match(correo): return "bien"
    else:return "mal"""""

    """if regexCorreo.match("carlos98frances@gmail.com"):return "bien"
    else:return "mal"""""
    # fin pruebas regex


# La funcionalidad de esta ruta se explica en README.txt
@app.route("/usuarios")
def mostrar_usuarios():
    return listaUsuarios


# La funcionalidad de esta ruta se explica en README.txt
@app.route("/usuarios/<user>")
def mostrar_usuario(user:str):
    # recorremos la los usuarios dentro de la lista de usuarios y devolvemos el primer usuario encontrado que
    # sea igual que el del parametro introducido
    for usuario in listaUsuarios["Usuarios"]:
        if usuario["usuario"] == user:
            return usuario

    # si no ha habido coincidencias, se retorna un error
    return "El usuario introducido no existe"


# La funcionalidad de esta ruta se explica en README.txt
@app.route("/log_usuario/<user>/<passw>")
def log_usuario(user:str,passw:str):
    # recorremos la los usuarios dentro de la lista de usuarios y devolvemos el primer usuario encontrado que
    # sea igual que el del parametro introducido y cuya contraseña coincida con la introducida por parámetro
    for usuario in listaUsuarios["Usuarios"]:
        if usuario["usuario"] == user and usuario["contraseña"] == passw:
            return usuario

        # si no ha habido coincidencias, se retorna un error
        else: return "LoG in fallido, comprueba tus datos"