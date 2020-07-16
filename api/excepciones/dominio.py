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
    
class No_hay_datos(Exception):
    def __init__(self):
        super().__init__(self)
        self.codigo = 204
        self.payload = None

    def generar_respuesta(self):
        response = dict(self.payload or ())
        response["message"] = "no hay datos que mostrar"
        return(response)

class No_sabe_que_buscar(Exception):
    def __init__(self):
        super().__init__(self)
        self.codigo = 403
        self.payload = None

    def generar_respuesta(self):
        response = dict(self.payload or ())
        response["message"] = "no hay datos que mostrar"
        return(response)

