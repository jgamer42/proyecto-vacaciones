from bd.singelton import Singelton
class Modelo_base:

    def __init__(self,datos):
        self.conexion =  Singelton().singelton()
        self.datos = datos
        self.config={
            "tabla":"tabla",
            "campos":[]
        }
        
        
    def insertar(self):
        salida = self.conexion.insertar(self.config,self.datos)
        return(salida)

    def eliminar(self):
        print(self.datos)
        salida = self.conexion.eliminar(self.config,self.datos)
        return (salida) 

    def actualizar(self):
        salida = self.conexion.actualizar(self.config,self.datos)
        return(salida)

    def info(self):
        print(self.datos,"\n",self.config)