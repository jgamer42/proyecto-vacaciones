from flask import Flask , render_template, jsonify
import sys
sys.path.append("./src")
sys.path.append("./bd")
from controllers import caso1
from singelton import Singelton
app = Flask(__name__)
@app.route("/")
def index():
    a = Singelton().singelton()
    a.consulta_prueba()
    return render_template("index.html")

@app.route("/prueba" , methods=["GET"])
def prueba():
    respuesta = [{"mensaje":"este es una consulta de prueba","dato":2}]
    return jsonify(respuesta)

if __name__ == "__main__":
    app.run()
