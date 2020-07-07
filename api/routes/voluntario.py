from flask import render_template, jsonify, request,abort
from api import app
from src.entities.voluntario import Voluntario
from bd.singelton import Singelton



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
    return jsonify(datos)

@app.route("/voluntario/consultar/<string:cedula>",methods=["GET"])
def consultar_voluntario_especifico(cedula):
    conexion = Singelton().singelton()
    dato = {"cedula":cedula}
    datos = conexion.consultar_especifico("voluntario","cedula",dato)
    if (datos == []):
        response = jsonify("no hay datos para mostrar")
        response.status_code = 204
    else:
        consulta_horas = {
            "tabla":"actividad",
            "campo":"duracion",
            "buscar":"voluntario",
            "voluntario":datos[0][0]
        }
        horas = conexion.consultar_campo(consulta_horas)
        total_horas = 0
        for hora in horas:
            total_horas += hora[0]
        consulta_programa = {
            "tabla":"programa",
            "campo":"nombre",
            "buscar":"id",
            "id":datos[0][4]
        }
        programa = conexion.consultar_campo(consulta_programa)
        salida = {
            "cedula":datos[0][0],
            "nombre":datos[0][1],
            "apellido":datos[0][2],
            "genero":datos[0][3],
            "programa":programa[0][0],
            "correo":datos[0][5],
            "telefono":datos[0][6],
            "horas":total_horas
        }
        response = jsonify(salida)
        response.status_code=201
    return(response)