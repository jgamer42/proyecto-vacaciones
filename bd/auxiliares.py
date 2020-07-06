from psycopg2 import sql
def componer_cadena(campos):
    cadena = []
    for campo in campos:
        aux = sql.Composed([sql.Identifier(campo),sql.Placeholder(campo)])
        aux = sql.SQL(" = ").join(aux)
        cadena.append(aux)
    salida = sql.SQL(" , ").join(cadena)
    return (salida)


