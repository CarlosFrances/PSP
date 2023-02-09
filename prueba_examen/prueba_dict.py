from flask import Flask,jsonify

app = Flask(__name__)

input="01234567L;LuisGonzalez;luisgonzalez@mail.com;656343576;12.5\n71476342J;MacarenaRamirez;macarena@a.com;6943321;8"

def obtenerDiccionario(texto:str):
    diccionario = {}
    textoSeparado=texto.split("\n")
    for i in textoSeparado:
        persona = i.split(";")
        dictPersona={
            "Nombre:":persona[1],
            "Correo":persona[2],
            "Telefono":persona[3]
        }
        diccionario[persona[0]]=dictPersona
    return diccionario

@app.route("/diccionario")
def get_diccionario():
    return jsonify(obtenerDiccionario(input))