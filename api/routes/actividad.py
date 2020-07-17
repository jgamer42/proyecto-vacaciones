from flask import render_template, jsonify, request
from api import app
from src.entities.actividad import Actividad
from bd.singelton import Singelton
from api.formater import formato_actividades

@app.route("/actividad/crear", methods = ["GET"])
def datos_para_crear_actividad():
    conexion = Singelton().singelton()
    proyectos = conexion.consultar_todo("proyecto")
    salida = {
        "proyectos":[]
    }
    for proyecto in proyectos:
        elemento = {
            "id": proyecto[0],
            "nombre":proyecto[1]
        }
        salida["proyectos"].append(elemento)
    salida = jsonify(salida)
    salida.status_code = 200 
    return salida

@app.route("/actividad/consultar",methods = ["GET"])
def consultar_todas_actividades():
    conexion = Singelton().singelton()
    actividades = conexion.consultar_todo("actividad")
    salida = []
    for actividad in actividades:
        aux = formato_actividades(actividad)
        salida.append(aux)
    salida  = jsonify(salida)
    salida.status_code = 200
    return (salida)

@app.route("/actividad/consultar/<int:id>" , methods = ['GET'])
    