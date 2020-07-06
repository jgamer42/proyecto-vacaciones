from flask import render_template, jsonify, request
from api import app
from src.controllers import caso1
from bd.singelton import Singelton


@app.route("/")
def index():
    config = {
        "tabla":"prueba",
        "campos":["dato1","dato2"],
        "buscar":"id"
    }
    datos = {
        "id":6,
        "dato1":20,
        "dato2":4
    }
    conexion = Singelton().singelton()
    conexion.actualizar(config,datos)
    return render_template("index.html")

@app.route("/prueba" , methods=["GET"])
def prueba():
    respuesta = []
    conexion = Singelton().singelton()
    datos = conexion.consultar("prueba")
    for dato in datos:
        diccionario = {
            "dato1": dato[0],
            "dato2": dato[1]
        }
        respuesta.append(diccionario)
    return jsonify(respuesta)

@app.route("/prueba" , methods=["POST"])
def ingresar():
    config = {
        "tabla":"prueba",
        "campos": ["dato1","dato2"],
    }
    datos = {
            "dato1": request.json["dato1"],
            "dato2": request.json["dato2"]
        }
    conexion = Singelton().singelton()
    respuesta = conexion.insertar(config,datos)
    return respuesta
