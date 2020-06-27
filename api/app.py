from flask import Flask , render_template
import sys
sys.path.append("../bd/")
sys.path.append("../src/")
#from conexion import conexion
from controllers import caso1
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)