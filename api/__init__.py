from flask import Flask , render_template, jsonify,request
from flask import Flask
app = Flask(__name__)

from api import routes

