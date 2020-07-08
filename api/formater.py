from bd.singelton import  Singelton

def formato_voluntario(datos):
    conexion = Singelton().singelton()
    consulta_horas = {
        "tabla":"actividad",
        "campo":"duracion",
        "buscar":"voluntario",
        "voluntario":datos[0]
    }
    horas = conexion.consultar_campo(consulta_horas)
    total_horas = 0
    for hora in horas:
        total_horas += hora[0]
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