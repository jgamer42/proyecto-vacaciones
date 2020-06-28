import psycopg2
import configparser
import os 
config = configparser.ConfigParser()
config.sections()
config.read(os.getcwd()+"/bd/config.ini")
class Conexion():
    instance = None
    def __init__(self):
        print("conexion creada")
        
    @staticmethod
    def consulta_prueba():
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        consulta.execute("SELECT * FROM prueba")
        datos = consulta.fetchall()
        print(datos)
        conexion.close()
