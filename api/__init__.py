from flask import Flask , render_template, jsonify,request
app = Flask(__name__)

#from api import otros
from api.routes import casos_de_uso,actividad,fundacion,proyecto,voluntario