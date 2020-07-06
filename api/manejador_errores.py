from api import app
from flask import request,jsonify
from api.excepciones.bd import Dato_inexistente
@app.errorhandler(Dato_inexistente)
def  not_found(error):
    response = jsonify(error.generar_respuesta())
    response.status_code = error.codigo
    return (response)