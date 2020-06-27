from flask import Flask , render_template
import sys
import os
sys.path.append(os.getcwd()+"/bd/")
sys.path.append(os.getcwd()+"/src/")
from conexion import conexion
from controllers import caso1
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
