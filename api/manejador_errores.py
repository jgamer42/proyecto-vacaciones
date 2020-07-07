from api import app
from flask import request,jsonify
#from api.excepciones.bd import Dato_inexistente, Error_inesperado ,Fallo_sql,Clave_foranea_inexistente,Clave_repetida
from api.excepciones.dominio import Error_validacion
import psycopg2

@app.errorhandler(Error_validacion)
def error_validacion(error):
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


