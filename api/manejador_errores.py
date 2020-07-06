from api import app
from flask import request,jsonify
from api.excepciones.bd import Dato_inexistente, Error_inesperado ,Fallo_sql
@app.errorhandler(Dato_inexistente)
def  no_hay_datos(error):
    response = jsonify(error.generar_respuesta())
    response.status_code = error.codigo
    return (response)

@app.errorhandler(Error_inesperado)
def inesperado(error):
    response = jsonify(error.generar_respuesta())
    response.status_code = error.codigo
    return (response)

@app.errorhandler(Fallo_sql)
def inesperado(error):
    response = jsonify(error.generar_respuesta())
    response.status_code = error.codigo
    return (response)