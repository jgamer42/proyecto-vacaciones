import psycopg2
import configparser
import os 
config = configparser.ConfigParser()
config.sections()
config.read(os.getcwd()+"/bd/config.ini")
class Conexion():
    instance = None
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config.read(os.getcwd()+"/bd/config.ini")
        
    @staticmethod
    def consulta_prueba():
        conexion = psycopg2.connect(host=self.config["db"]["host"],database=self.config["db"]["database"],user=self.config["db"]["user"],password=self.config["db"]["password"])
        consulta = conexion.cursor()
        consulta.execute("SELECT * FROM prueba")
        datos = consulta.fetchall()
        print(datos)
        conexion.close()
