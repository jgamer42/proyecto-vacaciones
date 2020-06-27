from flask import Flask , render_template
import sys
sys.path.append("./src")
sys.path.append("./bd")
from controllers import caso1
import conexion
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
