from flask import render_template, jsonify, request
from api import app
from bd.singelton import Singelton
from src.entities.fundacion import Fundacion

@app.route("/fundacion",methods=["GET"])
def consultar_fundacion():
    objeto = Actividad(1,"nombre",3,2,"descripcion",40)
    return("hola")

@app.route("/fundacion",methods=["POST"])
def crear_fundacion():
    datos={
        "id": request.json["id"],
        "voluntario": request.json["voluntario"],
        "proyecto": request.json["proyecto"],
        "nombre": request.json["nombre"],
        "descripcion": request.json["descripcion"],
        "duracion": request.json["duracion"]
    }
    objeto = Actividad(datos["id"],datos["nombre"],datos["proyecto"],datos["voluntario"],datos["descripcion"],datos["duracion"])
    return ("ok")
    
@app.route("/fundacion",methods=["PUT"])
def actualizar_fundacion():
    pass

@app.route("/fundacion",methods=["DELETE"])
def eliminar_fundacion():
    pass