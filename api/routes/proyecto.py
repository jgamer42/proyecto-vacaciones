from flask import render_template, jsonify, request
from api import app
from src.controllers import caso1
from bd.singelton import Singelton
