import flask
from flask import Flask, request, render_template
from flask_cors import CORS
from flask_mysqldb import MySQL
from config import config

api = Flask(__name__)
CORS(api)

conexion = MySQL(api)


# ruta para eliminar usuario. recibe por medio de request el dni y lo utiliza para eliminar dicho empleado de la db
@api.route("/delete-user",methods=["DELETE"])
def delete_user():
    try:
        cursor = conexion.connection.cursor()

        # recoger el dni del empleado a eliminar
        dni = request.json.get("dni")
        sql = "delete from empleados where dni='{0}'".format(dni)
        filas = cursor.execute(sql)
        conexion.connection.commit()

        # detectamos si se ha eliminado algun usuario o no y sacamos la respuesta correspondiente
        if filas > 0:
            return "Empleado con DNI:'{0}' eliminado".format(dni)
        else:
            return "no existe dicho empleado"
    except Exception as ex:
        return ex


# ruta para modificar un usuario
@api.route("/update-user",methods=["PUT"])
def update_user():

    texto = request.form

    textoSplit = texto.split(";")

    # comprobamos que el dni sea valido
    if validar_dni(textoSplit[0]) == False: # Aqui se incluirian el resto de validaciones
        return "usuario no valido"


    cursor = conexion.connection.cursor()
    sql="update empleados set dni='{0}',nombre='{1}',email='{2}',telefono='{3}',experiencia='{4}' where dni='{5}'".format(textoSplit[0],textoSplit[1],textoSplit[2],textoSplit[3],textoSplit[4],textoSplit[0])

    filas = cursor.execute(sql)
    conexion.connection.commit()

    if filas > 0:
        return "Empleado con DNI:'{0}' modificado".format(textoSplit[0])
    else:
        return "no existe dicho empleado"


# ruta para pedir empleados en funcion de la experiencia
@api.route("/get-users")
def get_users():
    #recoger el query string parameter, darle un tipo int y un valor por defecto de -1 (por si no se envia ningun parametro)
    experiencia = request.json.get("experiencia",[int],-1)

    cursor = conexion.connection.cursor()

    #si la experiencia es -1 significa que no se ha enviado ningun paaramerto y por lo tanto se obtienen todos los empleados
    if experiencia == -1:
        sql = "select * from empleados"
    #si la experiencia es diferente de -1 significa que se ha enviado un parametro y hay que filtrar los datos solicitados por experiencia
    else:
        sql = "select * from empleados where experiencia >= '{0}'".format(experiencia)

    #recogemos los datos obtenidos
    filas = cursor.execute(sql)
    conexion.connection.commit()

    #devolvemos los datos obtenidos
    return filas


@api.route("/add-users",methods=["POST"])
def obtenerUsuarios(texto:str):
    users = []
    usuarios = texto.split("\n")
    for idx, dato in enumerate(usuarios):
        for idx, dato2 in enumerate(dato):
            if idx == 0 or idx % 5 == 0:
                user = {"dni": "", "nombre": "", "email": "", "telefono": 0, "experiencia": 0.0}
                user["dni"] = dato
            if idx % 1 == 0:
                user["nombre"] = dato
            if idx % 2 == 0:
                user["email"] = dato
            if idx % 3 == 0:
                user["telefono"] = dato
            if idx % 4 == 0:
                user["experiencia"] = dato.split("\n")[0]
                users.append(user)

    for user in users:
        if validar_dni(user["dni"]) == True: # aqui se incluirian el resto de validaciones
            cursor = conexion.connection.cursor()
            sql = "insert into empleados ('{0}','{1}','{2}','{3}','{4}')".format(user["dni"],user["nombre"],user["email"],user["telefono"],user["experiencia"])
            cursor.execute(sql)
            conexion.connection.commit()

def validar_dni(dni:str):
    tabla_asignacion = 'TRWAGMYFPDXBNJZSQVHLCKE'

    # Comprobamos la longitud del DNI
    if len(dni) != 9:
        return False

    # Comprobamos que los primeros 8 caracteres sean dígitos
    if not dni[:8].isdigit():
        return False

    # Comprobamos que el último caracter sea una letra mayúscula
    if not dni[-1].isupper():
        return False

    # Calculamos el resto de la división entre el número formado por los primeros 8 caracteres del DNI y 23
    resto = int(dni[:8]) % 23

    # Comprobamos que la letra del DNI sea la correspondiente según la tabla de asignación
    if tabla_asignacion[resto] != dni[-1]:
        return False

    return True




def pagina_no_encontrada(error):
    return "<h1>La pagina que intentas buscar no existe</h1>",404




if __name__ == '__main__':
    api.config.from_object(config["development"])
    api.register_error_handler(404, pagina_no_encontrada)
    api.run()
