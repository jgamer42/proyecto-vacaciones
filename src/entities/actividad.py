from src.entities.modelo_base import Modelo_base
class Actividad(Modelo_base):
    def __init__ (self,datos):
        super().__init__(datos)
        self.config = {
            "tabla":"actividad",
            "campos":["id","voluntario","proyecto","nombre","descripcion","duracion","fecha"]
        }
        self.info()