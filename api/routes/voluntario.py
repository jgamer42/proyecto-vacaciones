from flask import render_template, jsonify, request,abort
from api import app
from src.entities.voluntario import Voluntario
from bd.singelton import Singelton
from api.excepciones.bd import Dato_inexistente ,Error_inesperado,Fallo_sql


@app.route("/voluntario/crear",methods=['POST'])
def crear_voluntario():
    nuevo_voluntario = {
        "cedula":request.json["cedula"],
        "nombre":request.json["nombre"],
        "apellido":request.json["apellido"],
        "genero":request.json["genero"],
        "programa":request.json["programa"],
        "correo":request.json["correo"],
        "telefono":request.json["telefono"]
    }
    objeto = Voluntario(nuevo_voluntario)
    objeto.insertar()
    return ("insertado con exito")

@app.route("/voluntario/eliminar", methods=["DELETE"])
def eliminar_voluntario():
    guia = {"cedula":request.json["cedula"]}
    objeto = Voluntario(guia)
    respuesta = objeto.eliminar()
    if(respuesta == 1):
        raise Fallo_sql()
    elif (respuesta == 3):
        raise Error_inesperado()
    else:
        salida = jsonify("eliminado con exito")
        salida.status_code = 201
    return (salida)

@app.route("/voluntario/actualizar", methods=["PUT"])
def actualizar_voluntario():
    nuevos_datos = {
        "cedula":request.json["cedula"],
        "nombre":request.json["nombre"],
        "apellido":request.json["apellido"],
        "genero":request.json["genero"],
        "programa":request.json["programa"],
        "correo":request.json["correo"],
        "telefono":request.json["telefono"]
    }
    objeto = Voluntario(nuevos_datos)
    objeto.actualizar()
    return("actualizado con exito")

@app.route("/voluntario/consultar",methods=["GET"])
def consultar_voluntario_todos():
    conexion = Singelton().singelton()
    datos = conexion.consultar_todo("voluntario")
    return jsonify(datos)

@app.route("/voluntario/consultar/<string:cedula>",methods=["GET"])
def consultar_voluntario_especifico(cedula):
    conexion = Singelton().singelton()
    dato = {"cedula":cedula}
    datos = conexion.consultar_especifico("voluntario","cedula",dato)
    if(datos == []):
        raise Dato_inexistente
    else:
        response = jsonify({"datos":datos})
        response.status_code=201
        return(response)