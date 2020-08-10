from bd.singelton import  Singelton
from api.aux import organizar,formatear
import configparser
import os

def formato_voluntario(datos):
    #carga la configuracion de la bd y las consultas
    queries = configparser.ConfigParser()
    queries.sections()
    queries.read(os.getcwd()+"/api/queries/formato_voluntarios.conf")
    conexion = Singelton().singelton()
    #determina las horas de servicio de un voluntario
    consulta_actividades = dict(queries["acitivades"])
    consulta_actividades["voluntario"]=datos[0]
    lista_actividades = conexion.consultar_campo(consulta_actividades)
    total_horas = 0
    for actividad in lista_actividades:
        consulta_horas = dict(queries["horas"])
        consulta_horas["id"]=actividad
        hora_actividad = conexion.consultar_campo(consulta_horas)
        total_horas += hora_actividad[0][0]
    #determina el programa del voluntario
    consulta_programa = dict(queries["programa"])
    consulta_programa["id"] = datos[4]
    programa = conexion.consultar_campo(consulta_programa)
    #formatea el voluntario
    voluntario = {
        "cedula":datos[0],
        "nombre":datos[1],
        "apellido":datos[2],
        "genero":datos[3],
        "programa":programa[0][0],
        "correo":datos[5],
        "telefono":datos[6],
        "horas":total_horas
    }
    return (voluntario)

def formato_proyecto(datos):
    queries = configparser.ConfigParser()
    queries.sections()
    queries.read(os.getcwd()+"/api/queries/formato_proyectos.conf")
    conexion = Singelton().singelton()
    consulta_lista_actividades = dict(queries["lista_actividades"])
    consulta_lista_actividades["proyecto"] = datos[0]
    consulta_lista_ods = dict(queries["lista_ods"])
    consulta_lista_ods["proyecto"] = datos[0]
    consulta_lista_sedes = dict(queries["lista_sedes"])
    consulta_lista_sedes["proyecto"]=datos[0]
    consulta_lista_fundaciones = dict(queries["lista_fundaciones"])
    consulta_lista_fundaciones["proyecto"] = datos[0]
    lista_actividades = conexion.consultar_especifico(consulta_lista_actividades)
    lista_actividades = organizar(lista_actividades)
    lista_relacion_ods = conexion.consultar_campo(consulta_lista_ods)
    lista_relacion_ods = organizar(lista_relacion_ods)
    lista_relacion_sedes = conexion.consultar_campo(consulta_lista_sedes)
    lista_relacion_sedes = organizar(lista_relacion_sedes)
    lista_relacion_fundaciones = conexion.consultar_campo(consulta_lista_fundaciones)
    lista_relacion_fundaciones = organizar(lista_relacion_fundaciones)
    consulta_lista_ods = dict(queries["ods"])
    consulta_lista_ods["lista"] = tuple(lista_relacion_ods)
    consulta_lista_sedes = dict(queries["sedes"])
    consulta_lista_sedes["lista"]=tuple(lista_relacion_sedes)
    consulta_lista_fundaciones = dict(queries["fundaciones"])
    consulta_lista_fundaciones["lista"] = tuple(lista_relacion_fundaciones)
    lista_aux_sedes = formatear(consulta_lista_sedes)
    lista_sedes=[]
    for sede in lista_aux_sedes:
        sede = formato_sede(sede)
        lista_sedes.append(sede)
    lista_aux_ods = formatear(consulta_lista_ods)
    lista_ods = []
    for ods in lista_aux_ods:
        ods = formato_ods(ods)
        lista_ods.append(ods)
    lista_aux_fundaciones = formatear(consulta_lista_fundaciones)
    lista_fundaciones = []
    for fundacion in lista_aux_fundaciones:
        fundacion = formato_fundacion(fundacion)
        lista_fundaciones.append(fundacion)
    lista_aux_actividades = lista_actividades
    lista_actividades = []
    for actividad in lista_aux_actividades:
        actividad = formato_actividades(actividad)
        lista_actividades.append(actividad)
    salida = {
        "id":datos[0],
        "nombre":datos[1],
        "descripcion":datos[2],
        "inicio":datos[3],
        "fin":datos[4],
        "actividades":lista_actividades,
        "ods":lista_ods,
        "sedes":lista_sedes,
        "fundaciones":lista_fundaciones
    }
    return(salida)

def formato_actividades(datos):
    queries = configparser.ConfigParser()
    queries.sections()
    queries.read(os.getcwd()+"/api/queries/formato_actividades.conf")
    conexion = Singelton().singelton()
    consulta_proyectos = dict(queries["proyectos"])
    consulta_proyectos["id"] = datos[1]
    consulta_lista_participantes = dict(queries["lista_participantes"])
    consulta_lista_participantes["actividad"] = datos[0]
    nombre_proyecto = conexion.consultar_campo(consulta_proyectos)
    lista_relacion = conexion.consultar_campo(consulta_lista_participantes)
    lista_relacion = organizar(lista_relacion)
    consulta_lista_participantes = dict(queries["participantes"])
    consulta_lista_participantes["lista"]=tuple(lista_relacion)
    lista_participantes = []
    if(lista_relacion == []):
        pass
    else:
        lista_participantes = conexion.consulta_con_lista(consulta_lista_participantes)
        lista_participantes = organizar(lista_participantes)
    salida = {
        "id":datos[0],
        "proyecto":nombre_proyecto[0][0],
        "nombre":datos[2],
        "descripcion":datos[3],
        "duracion":datos[4],
        "fecha":datos[5],
        "participantes":lista_participantes
    }
    return (salida)

def formato_ods(datos):
    salida = {
        "id":datos[0],
        "nombre":datos[1],
        "referencia":datos[2]
    }
    return(salida)

def formato_fundacion(datos):
    salida = {
        "id":datos[0],
        "nombre":datos[1],
        "direccion":datos[2]
    }
    return(salida)

def formato_sede(datos):
    salida = {
        "id":datos[0],
        "nombre":datos[1],
        "direccion":datos[2],
        "director":datos[3],
        "telefono":datos[4]
    }
    return(salida)

def formato_programa(datos):
    salida = {
        "id":datos[0],
        "nombre":datos[1]
    }
    return(salida)