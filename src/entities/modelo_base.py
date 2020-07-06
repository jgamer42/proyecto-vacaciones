from bd.singelton import Singelton
class Modelo_base:

    def __init__(self,datos):
        self.conexion =  Singelton().singelton()
        self.datos = datos
        self.config={
            "tabla":"tabla",
            "campos":[]
        }

    def consultar(self):
        datos = self.conexion.consultar(self.config["tabla"])
        return(datos)

    def insertar(self):
        self.conexion.insertar(self.config,self.datos)
        return("ok")

    def eliminar(self):
        config_borrar= {
            "referencia":"id",
            "datos":self.datos["id"]
        }
        self.conexion.eliminar(self.config,config_borrar)
        return ("ok") 

    def actualizar(self):
        pass

    def info(self):
        print(self.datos,"\n",self.config)