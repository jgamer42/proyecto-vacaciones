from bd.singelton import  Singelton
from api.aux import organizar,formatear
def formato_voluntario(datos):
    conexion = Singelton().singelton()
    consulta_actividades = {
        "tabla":"actividad_voluntario",
        "campo":"actividad",
        "buscar":"voluntario",
        "voluntario":datos[0]
    }
    lista_actividades = conexion.consultar_campo(consulta_actividades)
    total_horas = 0
    for actividad in lista_actividades:
        consulta_horas={
            "tabla":"actividad",
            "campo":"duracion",
            "buscar":"id",
            "id":actividad
        }
        hora_actividad = conexion.consultar_campo(consulta_horas)
        total_horas += hora_actividad[0][0]
    consulta_programa = {
        "tabla":"programa",
        "campo":"nombre",
        "buscar":"id",
        "id":datos[4]
    }
    programa = conexion.consultar_campo(consulta_programa)
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

def formato_programa(datos):
    salida = {
        "id":datos[0],
        "nombre":datos[1]
    }
    return(salida)

def formato_proyecto(datos):
    conexion = Singelton().singelton()
    consulta_lista_actividades={
        "tabla":"actividad",
        "referencia":"proyecto",
        "proyecto":datos[0]
    }
    consulta_lista_ods = {
        "tabla":"ods_proyecto",
        "campo":"ods",
        "buscar":"proyecto",
        "proyecto":datos[0]
    }
    consulta_lista_sedes = {
        "tabla":"sede_proyecto",
        "campo":"sede",
        "buscar":"proyecto",
        "proyecto":datos[0]
    }
    consulta_lista_fundaciones = {
        "tabla":"proyecto_fundacion",
        "campo":"fundacion",
        "buscar":"proyecto",
        "proyecto":datos[0]
    }
    lista_actividades = conexion.consultar_especifico(consulta_lista_actividades)
    lista_actividades = organizar(lista_actividades)
    lista_relacion_ods = conexion.consultar_campo(consulta_lista_ods)
    lista_relacion_ods = organizar(lista_relacion_ods)
    lista_relacion_sedes = conexion.consultar_campo(consulta_lista_sedes)
    lista_relacion_sedes = organizar(lista_relacion_sedes)
    lista_relacion_fundaciones = conexion.consultar_campo(consulta_lista_fundaciones)
    lista_relacion_fundaciones = organizar(lista_relacion_fundaciones)
    consulta_lista_ods={
        "tabla":"ods",
        "buscar":"id",
        "datos":"lista",
        "lista":tuple(lista_relacion_ods)
    }
    consulta_lista_sedes = {
        "tabla":"sede",
        "buscar":"id",
        "datos":"lista",
        "lista":tuple(lista_relacion_sedes)
    }
    consulta_lista_fundaciones={
        "tabla":"fundacion",
        "buscar":"id",
        "datos":"lista",
        "lista":tuple(lista_relacion_fundaciones)
    }
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
    conexion = Singelton().singelton()
    consulta_proyectos = {
        "tabla":"proyecto",
        "campo":"nombre",
        "buscar":"id",
        "id":datos[1]
    }
    consulta_lista_participantes = {
        "tabla":"actividad_voluntario",
        "campo":"voluntario",
        "buscar":"actividad",
        "actividad":datos[0]
    }
    nombre_proyecto = conexion.consultar_campo(consulta_proyectos)
    lista_relacion = conexion.consultar_campo(consulta_lista_participantes)
    lista_relacion = organizar(lista_relacion)
    consulta_lista_participantes = {
        "tabla":"voluntario",
        "campo":"nombre",
        "buscar":"cedula",
        "datos":"lista",
        "lista":tuple(lista_relacion)
    }
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
