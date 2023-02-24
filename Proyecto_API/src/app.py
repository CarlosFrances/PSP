# base de datos(api_flask curso[codigo(char[6]), nombre(varchar[30]), creditos(tinyint[1])])

from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

conexion = MySQL(app)

def pagina_no_encontrada(error):
    return "<h1>La pagina que intentas buscar no existe</h1>",404
@app.route("/")
def index():
    return "hola"

@app.route("/cursos")
def listar_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql = "select * from curso"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos =[]
        for fila in datos:
            curso={"codigo":fila[0],"nombre":fila[1],"creditos":fila[2]}
            cursos.append(curso)
        return jsonify({"cursos":cursos,"mensaje":"Cursos listados."})
    except Exception as ex:
        return jsonify({"mensaje":"Error"})

@app.route("/cursos/<codigo>", methods=["GET"])
def leer_curso(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "select * from curso where codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            curso={"codigo":datos[0],"nombre":datos[1],"creditos":datos[2]}
            return jsonify({"curso":curso,"mensaje":"Curso encontrado."})
        else:
            return jsonify({"mensaje":"Error"})
    except Exception as ex:
        return jsonify({"mensaje":"Error"})


@app.route("/cursos", methods=["POST"])
def registrar_curso():
    try:
        #todo comprobar si existe el dato antes de intentar insertarlo y lanzar el error correspondiente si es el caso
        cursor = conexion.connection.cursor()
        sql = "insert into curso (codigo, nombre, creditos) values ('{0}','{1}','{2}')".format(request.json["codigo"],request.json["nombre"],request.json["creditos"])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({"mensaje":"Curso registrado"})
    except Exception as ex:
        return jsonify({"mensaje": "Error"})


@app.route("/cursos/<codigo>", methods=["DELETE"])
def eliminar_curso(codigo):
    try:
        #todo comprobar si existe el dato antes de intentar eliminarlo y lanzar el error correspondiente si es el caso
        cursor = conexion.connection.cursor()
        sql = "delete from curso where codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({"mensaje":"Curso eliminado"})
    except Exception as ex:
        return jsonify({"mensaje": "Error"})


@app.route("/cursos/<codigo>", methods=["PUT"])
def actualizar_curso(codigo):
    try:
        #todo comprobar si existe el dato antes de intentar insertarlo y lanzar el error correspondiente si es el caso
        cursor = conexion.connection.cursor()
        sql = "update curso set nombre='{0}', creditos='{1}' where codigo = '{2}'".format(request.json["nombre"],request.json["creditos"], codigo)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({"mensaje":"Curso actualizado"})
    except Exception as ex:
        return jsonify({"mensaje": "Error"})


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()