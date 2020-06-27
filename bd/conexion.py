import psycopg2
import configparser
config = configparser.ConfigParser()
config.sections()
config.read("bd/config.ini")

class conexion():
    def __init__(self):
        self.conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        self.consulta = self.conexion.cursor()
        self.consulta.execute("SELECT * FROM prueba")
        self.datos = self.consulta.fetchall()
        print(self.datos)
        self.conexion.close()
a = conexion()