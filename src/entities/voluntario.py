from src.entities.modelo_base import Modelo_base
from cerberus import Validator
class Voluntario(Modelo_base):
    def __init__ (self,datos):
        super().__init__(datos)
        self.config = {
            "tabla":"voluntario",
            "campos":["cedula","nombre","apellido","genero","programa","correo","telefono"],
            "buscar":"cedula"
        }
        self.schema = {
            "cedula":{"type":"string","required":True},
            "nombre":{"type":"string","required":False},
            "apellido":{"type":"string","required":False},
            "genero":{"type":"string","required":False},
            "programa":{"type":"integer", "min":1,"required":False},
            "correo":{"type":"string","required":False,"regex":"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"},
            "telefono":{"type":"string","required":False,"minlength":10}
        }
        self.validador = Validator(self.schema)
        if(self.validador.validate(datos)):
            print("objeto creado de manera exitosa")
            self.info()
        else:
            print("error al crearlo")
            print(self.validador.errors)
