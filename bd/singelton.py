from .conexion import Conexion

class Singelton():
    def __init__(self):
        self.cls = Conexion

    def singelton(self):
        if(not self.cls.__instance):
            self.cls.__instace = self.cls
        return(self.cls)