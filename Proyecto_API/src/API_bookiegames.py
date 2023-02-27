import flask
from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
from config import config

api = Flask(__name__)

conexion = MySQL(api)

def pagina_no_encontrada(error):
    return "<h1>La pagina que intentas buscar no existe</h1>",404

@api.route("/")
def index():
    return flask.render_template("index.html")


@api.route("/videojuegos")
def videojuegos_home():
    return flask.render_template("videojuegos_home.html")




@api.route("/videojuegos/agregar")
def videojuegos_agregar():
    return flask.render_template("videojuegos_agregar.html")

@api.route("/videojuegos/agregar",methods=["POST"])
def videojuegos_agregar_bd():
    try:
        cursor = conexion.connection.cursor()
        data=request.form
        sql = "insert into videojuegos (nombre, imagen, nota) values ('{0}','{1}','{2}')".format(data["nombre"],
                                                                                                   data["imagen"],
                                                                                                   data["nota"])
        filas = cursor.execute(sql)
        conexion.connection.commit()
        if filas > 0:
            return flask.render_template("videojuegos_correcto.html")
        else:
            return flask.render_template("videojuegos_error.html")
    except Exception as ex:
        return ex


@api.route("/videojuegos/eliminar")
def videojuegos_eliminar():
    cursor = conexion.connection.cursor()
    sql = "select * from videojuegos"
    cursor.execute(sql)
    filas = cursor.fetchall()
    return flask.render_template("videojuegos_eliminar.html",resultados=filas)

@api.route("/videojuegos/eliminar", methods=["DELETE"])
def videojuegos_eliminar_db():
    try:
        cursor = conexion.connection.cursor()
        data=request.get_json()
        sql = "delete from videojuegos where nombre='{0}'".format(data["nombre"])
        cursor.execute(sql)
        conexion.connection.commit()
    except Exception as ex:
        return ex


@api.route("/videojuegos/ver_todos")
def videojuegos_ver_todos():
    try:
        cursor = conexion.connection.cursor()
        sql = "select * from videojuegos"
        cursor.execute(sql)
        filas = cursor.fetchall()
        return flask.render_template("videojuegos_ver_todos.html",resultados=filas)
    except Exception as ex:
        return ex


@api.route("/videojuegos/modificar")
def videojuegos_modificar():
    try:
        cursor = conexion.connection.cursor()
        sql = "select * from videojuegos"
        cursor.execute(sql)
        filas = cursor.fetchall()
        return flask.render_template("videojuegos_modificar.html", resultados=filas)
    except Exception as ex:
        return ex


@api.route("/videojuegos/modificar", methods=["PUT"])
def videojuegos_modificar_db():
    try:
        cursor = conexion.connection.cursor()
        data=request.get_json()
        sql = "update videojuegos set nombre='{0}',nota='{1}',imagen='{2}' where nombre = '{3}'".format(data["nombre"],data["nota"],data["imagen"],data["nombre_original"])
        filas = cursor.execute(sql)
        conexion.connection.commit()
    except Exception as ex:
        return ex


@api.route("/videojuegos/correcto")
def videojuegos_correcto():
    return render_template("videojuegos_correcto.html")


@api.route("/libros")
def libros_home():
    return flask.render_template("libros_home.html")

@api.route("/libros/agregar")
def libros_agregar():
    return flask.render_template("libros_agregar.html")


@api.route("/libros/agregar",methods=["POST"])
def libros_agregar_bd():
    try:
        cursor = conexion.connection.cursor()
        data=request.form
        sql = "insert into libros (nombre, imagen, nota) values ('{0}','{1}','{2}')".format(data["nombre"],
                                                                                                   data["imagen"],
                                                                                                   data["nota"])
        filas = cursor.execute(sql)
        conexion.connection.commit()
        if filas > 0:
            return flask.render_template("libros_correcto.html")
        else:
            return flask.render_template("libros_error.html")
    except Exception as ex:
        return ex

@api.route("/libros/ver_todos")
def libros_ver_todos():
    try:
        cursor = conexion.connection.cursor()
        sql = "select * from libros"
        cursor.execute(sql)
        filas = cursor.fetchall()
        return flask.render_template("libros_ver_todos.html", resultados=filas)
    except Exception as ex:
        return ex


@api.route("/libros/eliminar")
def libros_eliminar():
    cursor = conexion.connection.cursor()
    sql = "select * from libros"
    cursor.execute(sql)
    filas = cursor.fetchall()
    return flask.render_template("libros_eliminar.html",resultados=filas)


@api.route("/libros/eliminar", methods=["DELETE"])
def libros_eliminar_db():
    try:
        cursor = conexion.connection.cursor()
        data=request.get_json()
        sql = "delete from libros where nombre='{0}'".format(data["nombre"])
        cursor.execute(sql)
        conexion.connection.commit()
    except Exception as ex:
        return ex


@api.route("/libros/correcto")
def libros_correcto():
    return render_template("libros_correcto.html")



@api.route("/libros/modificar")
def libros_modificar():
    try:
        cursor = conexion.connection.cursor()
        sql = "select * from libros"
        cursor.execute(sql)
        filas = cursor.fetchall()
        return flask.render_template("libros_modificar.html", resultados=filas)
    except Exception as ex:
        return ex



@api.route("/libros/modificar", methods=["PUT"])
def libros_modificar_db():
    try:
        cursor = conexion.connection.cursor()
        data=request.get_json()
        sql = "update libros set nombre='{0}',nota='{1}',imagen='{2}' where nombre = '{3}'".format(data["nombre"],data["nota"],data["imagen"],data["nombre_original"])
        cursor.execute(sql)
        conexion.connection.commit()
    except Exception as ex:
        return ex



if __name__ == "__main__":
    api.config.from_object(config["development"])
    api.register_error_handler(404,pagina_no_encontrada)
    api.run()