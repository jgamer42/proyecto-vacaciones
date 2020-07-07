class Error_validacion(Exception):
    def __init__(self,mensaje):
        super().__init__(self)
        self.message=mensaje
        self.codigo = 409
        self.payload = None

    def generar_respuesta(self):
        response = dict(self.payload or ())
        response["info"] = "un campo no cumplio la condicion"
        response["message"] = self.message
        return(response)
