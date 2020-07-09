from datetime import datetime

def cast_fecha(cadena):
    return datetime.strptime(cadena,'%Y-%m-%d')