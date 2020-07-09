from src.entities.modelo_base import Modelo_base
from api.excepciones.dominio import Error_validacion
from src.auxiliares import cast_fecha
from cerberus import Validator
class Proyecto(Modelo_base):
    def __init__ (self,datos):
        super().__init__(datos)
        self.config = {
            "tabla":"proyecto",
            "campos":["nombre","descripcion","fecha_inicio","fecha_final"],
            "buscar":"id"
        }
        self.schema = {
            "id":{"type":"integer","required":False},
            "nombre":{"type":"string","required":False},
            "descripcion":{"type":"string","required":False},
            "fecha_inicio":{"type":"datetime","coerce":cast_fecha ,"required":False},
            "fecha_final":{"type":"datetime","coerce":cast_fecha ,"required":False},
        }
        self.validador = Validator(self.schema)
        if(not self.validador.validate(datos)):
            raise Error_validacion(self.validador.errors)
        else:
            self.info()