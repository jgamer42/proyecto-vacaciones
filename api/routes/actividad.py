from flask import render_template, jsonify, request
from api import app
from src.controllers import caso1
from src.entities.actividad import Actividad
from bd.singelton import Singelton

@app.route("/actividad",methods=["GET"])
def consultar():
    return("hola")

@app.route("/actividad",methods=["POST"])
def crear():
    datos={
        "id": request.json["id"],
        "voluntario": request.json["voluntario"],
        "proyecto": request.json["proyecto"],
        "nombre": request.json["nombre"],
        "descripcion": request.json["descripcion"],
        "duracion": request.json["duracion"],
        "fecha":request.json["fecha"]
    }
    objeto = Actividad(datos)
    return ("ok")
    
@app.route("/actividad",methods=["PUT"])
def actualizar():
    pass

@app.route("/actividad",methods=["DELETE"])
def eliminar():
    pass
