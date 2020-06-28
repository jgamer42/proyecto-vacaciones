from flask import Flask , render_template, jsonify,request
import sys
sys.path.append("./src")
sys.path.append("./bd")
from controllers import caso1
from singelton import Singelton
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prueba" , methods=["GET"])
def prueba():
    respuesta = []
    consulta = Singelton().singelton()
    consulta.consulta_prueba()
    for dato in consulta:
        diccionario = {
            "dato1": dato[0],
            "dato2": dato[1]
        }
        respuesta.append(diccionario)
    #return jsonify(respuesta)
    return "hola"

@app.route("/prueba" , methods=["POST"])
def ingresar():
    datos = {
        "dato1":request.json["dato1"],
        "dato2":request.json["dato2"]
    }
    conexion = Singelton().singelton()
    conexion.insertar_prueba(datos)
    return "datos ingresados con exito"

if __name__ == "__main__":
    app.run()
