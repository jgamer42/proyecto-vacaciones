from flask import render_template, jsonify, request,make_response
from api import app
from api.excepciones.dominio import No_sabe_que_buscar,No_hay_datos
from api.formater import formato_proyecto,formato_ods,formato_sede,formato_fundacion
from src.entities.proyecto import Proyecto
from bd.singelton import Singelton


@app.route("/proyecto/consultar",methods=["GET"])
def consultar_proyectos_todos():
    conexion = Singelton().singelton()
    datos = conexion.consultar_todo("proyecto")
    salida = []
    if(datos == []):
        raise  No_hay_datos()
    for dato in datos:
        aux = formato_proyecto(dato)
        salida.append(aux)
    salida = jsonify(salida)
    salida.status_code = 200
    return (salida)

@app.route("/proyecto/consultar/<int:id>",methods=["GET"])
def consultar_proyectos_especifico(id):
    conexion = Singelton().singelton()
    consulta={
        "tabla":"proyecto",
        "referencia":"id",
        "id":id
    }
    consulta = conexion.consultar_especifico(consulta)
    if (consulta == []):
        raise No_hay_datos()
    salida = formato_proyecto(consulta[0])
    salida = jsonify(salida)
    salida.status_code = 200
    return (salida)

@app.route("/proyecto/crear",methods=["GET"])
def datos_crear_proyecto():
    conexion = Singelton().singelton()
    salida={
        "ods":[],
        "fundaciones":[],
        "sedes":[]
    }
    ods = conexion.consultar_todo("ods")
    fundaciones = conexion.consultar_todo("fundacion")
    sedes = conexion.consultar_todo("sede")
    for dato in ods:
        aux = formato_ods(dato)
        salida["ods"].append(aux)
    for fundacion in fundaciones:
        aux = formato_fundacion(fundacion)
        salida["fundaciones"].append(aux)
    for sede in sedes:
        aux = formato_sede(sede)
        salida["sedes"].append(aux)
    salida = jsonify(salida)
    salida.status_code = 200
    return(salida)

@app.route("/proyecto/crear", methods=["POST"])
def crear_proyecto():
    print(request.json)
    if not ("fecha_final" in request.json):
        nuevo_proyecto = {
            "nombre":request.json["nombre"],
            "descripcion":request.json["descripcion"],
            "fecha_inicio":request.json["fecha_inicio"],
            "fecha_final":request.json["fecha_inicio"],
            "lista_ods":request.json["lista_ods"],
            "sedes":request.json["sedes"],
            "fundaciones":request.json["fundaciones"]
        }
    else:
        print("hola entre por el else")
        nuevo_proyecto = {
            "nombre":request.json["nombre"],
            "descripcion":request.json["descripcion"],
            "fecha_inicio":request.json["fecha_inicio"],
            "fecha_final":request.json["fecha_final"],
            "lista_ods":request.json["lista_ods"],
            "sedes":request.json["sedes"],
            "fundaciones":request.json["fundaciones"]
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
                "fecha_final":request.json["fecha_inicio"],
                "sedes":request.json["sedes"],
                "fundaciones":request.json["fundaciones"],
                "lista_ods":request.json["lista_ods"]
            }
        else:
            nuevo_proyecto = {
                "id":request.json["id"],
                "nombre":request.json["nombre"],
                "descripcion":request.json["descripcion"],
                "fecha_inicio":request.json["fecha_inicio"],
                "fecha_final":request.json["fecha_final"],
                "sedes":request.json["sedes"],
                "fundaciones":request.json["fundaciones"],
                "ods":request.json["lista_ods"]
            }
        objeto = Proyecto(nuevo_proyecto)
        objeto.actualizar()
    else:
        raise No_sabe_que_buscar()
    salida = jsonify("datos ingresados con exito")
    salida.status_code = 201
    return(salida)