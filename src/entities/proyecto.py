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
            "buscar":"id",
            "actualizar":"id",
        }
        self.schema = {
            "id":{"type":"integer","required":False},
            "nombre":{"type":"string","required":False},
            "descripcion":{"type":"string","required":False},
            "fecha_inicio":{"type":"datetime","coerce":cast_fecha ,"required":False},
            "fecha_final":{"type":"datetime","coerce":cast_fecha ,"required":False},
            "sedes":{"type":'list', "required":False},
            "lista_ods":{"type":'list', "required":False},
            "fundaciones":{"type":'list',"required":False}
        }
        self.validador = Validator(self.schema)
        if(not self.validador.validate(datos)):
            raise Error_validacion(self.validador.errors)
        else:
            self.info()
    
    def insertar(self):
        super().insertar()
        key = self.conexion.consultar_todo("proyecto")
        key = key[len(key)-1]
        key = key[0]
        config_ods={
            "tabla":"ods_proyecto",
            "campos":["proyecto","ods"]
        }
        for objetivo in self.datos["lista_ods"]:
            datos={
                "proyecto":key,
                "ods":objetivo
            }
            self.conexion.insertar(config_ods,datos)
        config_sede={
            "tabla":"sede_proyecto",
            "campos":["proyecto","sede"]
        }
        for sede in self.datos["sedes"]:
            datos={
                "proyecto":key,
                "sede":sede
            }
            self.conexion.insertar(config_sede,datos)
        config_fundacion={
            "tabla":"proyecto_fundacion",
            "campos":["proyecto","fundacion"]
        }
        for fundacion in self.datos["fundaciones"]:
            datos={
                "proyecto":key,
                "fundacion":fundacion
            }
            self.conexion.insertar(config_fundacion,datos)

    def actualizar(self):
        config_ods = {
            "tabla":"ods_proyecto",
            "buscar":"proyecto"
        }
        config_sedes = {
            "tabla":"sede_proyecto",
            "buscar":"proyecto"
        }
        config_fundaciones = {
            "tabla":"proyecto_fundacion",
            "buscar":"proyecto"
        }
        datos={
            "proyecto":self.datos["id"]
        }
        self.conexion.eliminar(config_ods,datos)
        self.conexion.eliminar(config_sedes,datos)
        self.conexion.eliminar(config_fundaciones,datos)

        config_ods = {
            "tabla":"ods_proyecto",
            "campos":["proyecto","ods"]
        }
        for ods in self.datos["lista_ods"]:
            datos = {
                "proyecto":self.datos["id"],
                "ods":ods
            }
            self.conexion.insertar(config_ods,datos)

        config_sedes = {
            "tabla":"sede_proyecto",
            "campos":["proyecto","sede"]
        }
        for sede in self.datos["sedes"]:
            datos = {
                "proyecto":self.datos["id"],
                "sede":sede
            }
            self.conexion.insertar(config_sedes,datos)

        config_fundacion = {
            "tabla":"proyecto_fundacion",
            "campos":["proyecto","fundacion"]
        }
        for fundacion in self.datos["fundaciones"]:
            datos = {
                "proyecto":self.datos["id"],
                "fundacion":fundacion
            }
            self.conexion.insertar(config_fundacion,datos)
        super().actualizar()