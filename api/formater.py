from bd.singelton import  Singelton

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
    print(datos)
    conexion = Singelton().singelton()
    lista_relacion_actividades = conexio.consultar_campo()
    salida = {
        "id":datos[0],
        "nombre":datos[1],
        "descripcion":datos[2],
        "inicio":datos[3],
        "fin":datos[4]
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
