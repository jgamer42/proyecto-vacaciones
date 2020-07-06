from src.entities.modelo_base import Modelo_base
class Voluntario(Modelo_base):
    def __init__ (self,datos):
        super().__init__(datos)
        self.config = {
            "tabla":"voluntario",
            "campos":["cedula","nombre","apellido","genero","programa","correo","telefono"],
            "buscar":"cedula"
        }
        self.info()