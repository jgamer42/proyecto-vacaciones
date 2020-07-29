from src.entities.modelo_base import Modelo_base
from api.excepciones.dominio import Error_validacion
from cerberus import Validator
class Voluntario(Modelo_base):
    def __init__ (self,datos):
        super().__init__(datos)
        self.config = {
            "tabla":"voluntario",
            "campos":["cedula","nombre","apellido","genero","programa","correo","telefono"],
            "buscar":"cedula",
            "actualizar":"cedula_antigua"
        }
        self.schema = {
            "cedula":{"type":"string","required":True},
            "nombre":{"type":"string","required":False},
            "apellido":{"type":"string","required":False},
            "genero":{"type":"string","required":False},
            "programa":{"type":"integer", "min":1,"required":False},
            "correo":{"type":"string","required":False,"regex":"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"},
            "telefono":{"type":"string","required":False,"minlength":10},
            "cedula_antigua":{"type":"string","required":False},
        }
        self.validador = Validator(self.schema)
        if(not self.validador.validate(datos)):
            raise Error_validacion(self.validador.errors)
        #else:
            #self.info()