from api import app
from flask import request,jsonify
from api.excepciones.dominio import Error_validacion ,No_hay_datos, No_sabe_que_buscar
import psycopg2

@app.errorhandler(Error_validacion)
def error_validacion(error):
    response = jsonify(error.generar_respuesta())
    response.status_code = error.codigo
    return (response)

@app.errorhandler(No_sabe_que_buscar)
def error_busqueda(error):
    response = jsonify(error.generar_respuesta())
    response.status_code = error.codigo
    return (response)

@app.errorhandler(No_hay_datos)
def no_hay_datos(error):
    response = jsonify(error.generar_respuesta())
    response.status_code = error.codigo
    return (response)

@app.errorhandler(psycopg2.errors.UniqueViolation)
def error_id(error):
    response = jsonify("este dato ya existe")
    response.status_code = 400
    return (response)

@app.errorhandler(psycopg2.errors.ForeignKeyViolation)
def error_foranea(error):
    print(error)
    response = jsonify("clave foranea inexistente")
    response.status_code = 409
    return (response)


