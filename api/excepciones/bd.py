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

class Error_inesperado(Exception):
    def __init__(self):
        super().__init__(self)
        self.message="error inesperado en el servidor"
        self.codigo = 505
        self.payload = None

    def generar_respuesta(self):
        response = dict(self.payload or ())
        response["message"] = self.message
        return(response)

class Fallo_sql(Exception):
    def __init__(self):
        super().__init__(self)
        self.message="algo salio mal con el sql"
        self.codigo = 506
        self.payload = None

    def generar_respuesta(self):
        response = dict(self.payload or ())
        response["message"] = self.message
        return(response)
