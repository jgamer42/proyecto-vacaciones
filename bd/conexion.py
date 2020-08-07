import psycopg2
from psycopg2 import sql
import configparser
import os 
import bd.auxiliares as aux 
config = configparser.ConfigParser()
config.sections()
config.read(os.getcwd()+"/bd/config.ini")
class Conexion():
    instance = None
    def __init__(self):
        print("conexion creada")

    @staticmethod
    def consultar_todo(tabla):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        salida = None
        try:
            consulta.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(tabla)))
            datos = consulta.fetchall()
            salida = datos
        finally:
            consulta.close()
            conexion.close()
        return(salida)

    @staticmethod
    def consultar_especifico(config_sql):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        salida = None
        try:
            consulta.execute(sql.SQL("SELECT * FROM {tabla} WHERE {referencia} = {dato}").format(
                tabla = sql.Identifier(config_sql["tabla"]),
                referencia = sql.Identifier(config_sql["referencia"]),
                dato = sql.Placeholder(config_sql["referencia"])
                ),config_sql)
            datos = consulta.fetchall()
            salida = datos
        finally:
            consulta.close()
            conexion.close()
        return(salida)

    @staticmethod
    def consultar_campo(config_sql):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        salida = None
        try:
            consulta.execute(sql.SQL("SELECT {campo} FROM {tabla} WHERE {referencia} = {dato}").format(
                campo = sql.Identifier(config_sql["campo"]),
                tabla = sql.Identifier(config_sql["tabla"]),
                referencia = sql.Identifier(config_sql["buscar"]),
                dato = sql.Placeholder(config_sql["buscar"])
                ),config_sql)
            datos = consulta.fetchall()
            salida = datos
        finally:
            consulta.close()
            conexion.close()
        return(salida)
    
    @staticmethod
    def insertar(sql_config,datos):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        salida = 0
        try:
            str_consulta=sql.SQL("INSERT INTO {tabla} ({campos}) VALUES ({referencia})").format(
                tabla = sql.Identifier(sql_config["tabla"]),
                campos = sql.SQL(",").join(map(sql.Identifier,sql_config["campos"])),
                referencia = sql.SQL(",").join(map(sql.Placeholder,sql_config["campos"])),
            )
            consulta.execute(str_consulta,datos)
            conexion.commit()
        finally:
            consulta.close()
            conexion.close()
        return(salida)

    @staticmethod
    def eliminar(sql_config,datos):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        salida = 0
        try:
            str_consulta = sql.SQL("DELETE FROM {tabla} WHERE {campo} = {clave}").format(
                tabla = sql.Identifier(sql_config["tabla"]),
                campo = sql.Identifier(sql_config["buscar"]),
                clave = sql.Placeholder(sql_config["buscar"])
            )
            print(str_consulta.as_string(consulta))
            consulta.execute(str_consulta,datos)
            conexion.commit()
            
        finally:
            consulta.close()
            conexion.close()
        return (salida)
        
    @staticmethod
    def actualizar(sql_config,datos):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        try:
            str_consulta = sql.SQL("UPDATE {tabla} SET {data} WHERE {campo} = {referencia}").format(
                tabla = sql.Identifier(sql_config["tabla"]),
                data = aux.componer_cadena(sql_config["campos"]),
                campo = sql.Identifier(sql_config["buscar"]),
                referencia = sql.Placeholder(sql_config["actualizar"])
            )
            consulta.execute(str_consulta,datos)
            conexion.commit()
            print("exito")
        finally:
            consulta.close()
            conexion.close()

    @staticmethod
    def consulta_con_lista(config_sql):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        try:
            cadena_sql = sql.SQL("SELECT * FROM {tabla} WHERE {buscar} IN {datos}").format(    
                tabla = sql.Identifier(config_sql["tabla"]),
                buscar = sql.Identifier(config_sql["buscar"]),
                datos = sql.Placeholder(config_sql["datos"])
            )
            consulta.execute(cadena_sql,config_sql)
            datos = consulta.fetchall()
        finally:
            consulta.close()
            conexion.close()
        return datos