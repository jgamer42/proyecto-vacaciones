from flask import Flask , render_template, jsonify,request
from flask_cors import CORS ,cross_origin
app = Flask(__name__)
CORS(app)


#from api import otros
from api.routes import casos_de_uso,actividad,fundacion,proyecto,voluntario
from api import manejador_errores