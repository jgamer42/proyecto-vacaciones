from bd.singelton import  Singelton
def organizar(lista):
    salida = []
    for i in lista:
        salida.append(i[0])
    return(salida)

def formatear(config):
    if (config["lista"] == ()):
        salida=[]
    else:
        conexion = Singelton().singelton()
        salida = conexion.consulta_con_lista(config)
    return salida