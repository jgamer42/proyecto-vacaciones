from bd.singelton import  Singelton
from api.aux import organizar
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
    consulta_lista_actividades = {
        "tabla":"actividad",
        "campo":"nombre",
        "buscar":"proyecto",
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
    lista_actividades = conexion.consultar_campo(consulta_lista_actividades)
    lista_actividades = organizar(lista_actividades)
    lista_relacion_ods = conexion.consultar_campo(consulta_lista_ods)
    lista_relacion_ods = organizar(lista_relacion_ods)
    lista_relacion_sedes = conexion.consultar_campo(consulta_lista_sedes)
    lista_relacion_sedes = organizar(lista_relacion_sedes)
    consulta_lista_ods={
        "tabla":"ods",
        "campo":"nombre",
        "buscar":"id",
        "datos":"lista",
        "lista":tuple(lista_relacion_ods)
    }
    consulta_lista_sedes = {
        "tabla":"sede",
        "campo":"nombre",
        "buscar":"id",
        "datos":"lista",
        "lista":tuple(lista_relacion_sedes)
    }
    if(consulta_lista_sedes["lista"] == ()):
        lista_sede = None
    else:
        lista_sede = conexion.consulta_con_lista(consulta_lista_sedes)
        lista_sede = organizar(lista_sede)
    if(consulta_lista_ods["lista"] == ()):
        lista_ods = None
    else:
        lista_ods = conexion.consulta_con_lista(consulta_lista_ods)
        lista_ods = organizar(lista_ods)
    salida = {
        "id":datos[0],
        "nombre":datos[1],
        "descripcion":datos[2],
        "inicio":datos[3],
        "fin":datos[4],
        "actividades":lista_actividades,
        "ods":lista_ods,
        "sedes":lista_sede
    }
    return(salida)

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
