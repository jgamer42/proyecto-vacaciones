from flask import render_template, jsonify, request,abort,make_response
from api import app
from src.entities.voluntario import Voluntario
from bd.singelton import Singelton
from api.excepciones.dominio import No_hay_datos
from api.formater import formato_voluntario, formato_programa

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
    salida = jsonify("datos ingresados con exito")
    salida.status_code = 201
    return (salida)

@app.route("/voluntario/crear",methods=['GET'])
def datos_crear_voluntario():
    conexion = Singelton().singelton()
    datos = conexion.consultar_todo("programa")
    salida = []
    for dato in datos:
        aux = formato_programa(dato)
        salida.append(aux)
    salida = jsonify(salida)
    salida.status_code=200
    return(salida)

@app.route("/voluntario/eliminar", methods=["DELETE"])
def eliminar_voluntario():
    dato = {"cedula":request.json["cedula"]}
    objeto = Voluntario(dato)
    objeto.eliminar()
    salida = jsonify("eliminado con exito")
    salida.status_code = 200
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
    salida = jsonify("objeto actualizado con exito")
    salida.status_code = 200
    return(salida)

@app.route("/voluntario/consultar",methods=["GET"])
def consultar_voluntario_todos():
    conexion = Singelton().singelton()
    datos = conexion.consultar_todo("voluntario")
    salida = []
    if(datos == []):
        raise No_hay_datos()
    else:
        for dato in datos:
            voluntario = formato_voluntario(dato)
            salida.append(voluntario)
        response = jsonify(salida)
        response.status_code=200
    return jsonify(salida)

@app.route("/voluntario/consultar/<string:cedula>",methods=["GET"])
def consultar_voluntario_especifico(cedula):
    conexion = Singelton().singelton()
    dato = {"cedula":cedula}
    datos = conexion.consultar_especifico("voluntario","cedula",dato)
    if (datos == []):
        raise No_hay_datos()
    else:
        salida = formato_voluntario(datos[0])
        response = jsonify(salida)
        response.status_code=200
    return(response)