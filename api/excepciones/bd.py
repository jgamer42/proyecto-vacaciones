from flask import jsonify

class Dato_inexistente(Exception):
    def __init__(self):
        super().__init__(self)
        self.message="el dato que busca no existe"
        self.codigo = 209
        self.payload = None

    def generar_respuesta(self):
        response = dict(self.payload or ())
        response["message"] = self.message
        return(response)
