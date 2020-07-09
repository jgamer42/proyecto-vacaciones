from flask import render_template, jsonify, request
from api import app
from api.excepciones.dominio import NO_sabe_que_buscar
from src.entities.proyecto import Proyecto
from bd.singelton import Singelton

@app.route("/proyecto/crear", methods=["POST"])
def crear_proyecto():
    if not ("fecha_final" in request.json):
        nuevo_proyecto = {
            "nombre":request.json["nombre"],
            "descripcion":request.json["descripcion"],
            "fecha_inicio":request.json["fecha_inicio"],
            "fecha_final":request.json["fecha_inicio"]
        }
    else:
        nuevo_proyecto = {
            "nombre":request.json["nombre"],
            "descripcion":request.json["descripcion"],
            "fecha_inicio":request.json["fecha_inicio"],
            "fecha_final":request.json["fecha_final"]
        }
        
    objeto = Proyecto(nuevo_proyecto)
    objeto.insertar()
    salida = jsonify("datos ingresados con exito")
    salida.status_code = 201
    return(salida)

@app.route("/proyecto/eliminar",methods=["DELETE"])
def eliminar_proyecto():
    dato = {"id":request.json["id"]}
    objeto = Proyecto(dato)
    objeto.eliminar()
    salida = jsonify("eliminado con exito")
    salida.status_code = 200
    return (salida) 

@app.route("/proyecto/actualizar", methods=["PUT"])
def actualizar_proyecto():
    if "id" in request.json:
        if not ("fecha_final" in request.json):
            nuevo_proyecto = {
                "id":request.json["id"],
                "nombre":request.json["nombre"],
                "descripcion":request.json["descripcion"],
                "fecha_inicio":request.json["fecha_inicio"],
                "fecha_final":request.json["fecha_inicio"]
            }
        else:
            nuevo_proyecto = {
                "id":request.json["id"],
                "nombre":request.json["nombre"],
                "descripcion":request.json["descripcion"],
                "fecha_inicio":request.json["fecha_inicio"],
                "fecha_final":request.json["fecha_final"]
            }
        objeto = Proyecto(nuevo_proyecto)
        objeto.insertar()
    else:
        raise NO_sabe_que_buscar()
    salida = jsonify("datos ingresados con exito")
    salida.status_code = 201
    return(salida)