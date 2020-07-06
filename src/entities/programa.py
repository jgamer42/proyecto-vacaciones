from src.entities.modelo_base import Modelo_base
class Programa(Modelo_base):
    def __init__ (self,datos):
        super().__init__(datos)
        self.config = {
            "tabla":"actividad",
            "campos":["id","nombre","facultad"]
        }
        self.info()