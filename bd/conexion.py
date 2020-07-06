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
        except psycopg2.errors.UndefinedColumn:
            print("la columba no existe")
        except psycopg2.errors.UndefinedTable:
            print("la tabla no existe")
        except Exception:
            print("cuidado no sabemos porque exploto")
        finally:
            consulta.close()
            conexion.close()
        return(salida)
    
    def consultar_especifico(tabla,referencia,dato):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        salida = None
        try:
            consulta.execute(sql.SQL("SELECT * FROM {tabla} WHERE {referencia} = {dato}").format(
                tabla = sql.Identifier(tabla),
                referencia = sql.Identifier(referencia),
                dato = sql.Placeholder(referencia)
                ),dato)
            datos = consulta.fetchall()
            salida = datos
        except psycopg2.errors.UndefinedTable:
            salida = 1
        except Exception:
            salida = 2
        finally:
            consulta.close()
            conexion.close()
        return(salida)
    
    @staticmethod
    def insertar(sql_config,datos):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        try:
            str_consulta=sql.SQL("INSERT INTO {tabla} ({campos}) VALUES ({referencia})").format(
                tabla = sql.Identifier(sql_config["tabla"]),
                campos = sql.SQL(",").join(map(sql.Identifier,sql_config["campos"])),
                referencia = sql.SQL(",").join(map(sql.Placeholder,sql_config["campos"])),
                )
            consulta.execute(str_consulta,datos)
            conexion.commit()
        except psycopg2.errors.InvalidForeignKey:
            print("error al insertar")
        #except Exception:
            #print("cuidado no sabemos porque exploto")
        finally:
            consulta.close()
            conexion.close()
        return "ok"

    @staticmethod
    def eliminar(sql_config,datos):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        try:
            str_consulta = sql.SQL("DELETE FROM {tabla} WHERE {campo} = {clave}").format(
                tabla = sql.Identifier(sql_config["tabla"]),
                campo = sql.Identifier(sql_config["buscar"]),
                clave = sql.Placeholder(sql_config["buscar"])
            )
            consulta.execute(str_consulta,datos)
            conexion.commit()
        except Exception:
            print("cuidado no sabemos porque exploto")
        finally:
            consulta.close()
            conexion.close()

    @staticmethod
    def actualizar(sql_config,datos):
        conexion = psycopg2.connect(host=config["db"]["host"],database=config["db"]["database"],user=config["db"]["user"],password=config["db"]["password"])
        consulta = conexion.cursor()
        try:
            str_consulta = sql.SQL("UPDATE {tabla} SET {data} WHERE {campo} = {referencia}").format(
                tabla = sql.Identifier(sql_config["tabla"]),
                data = aux.componer_cadena(sql_config["campos"]),
                campo = sql.Identifier(sql_config["buscar"]),
                referencia = sql.Placeholder(sql_config["buscar"])
            )
            consulta.execute(str_consulta,datos)
            conexion.commit()
        except Exception:
            print("cuidado no sabemos porque exploto")
        finally:
            consulta.close()
            conexion.close()
