from flask import render_template, jsonify, request,make_response
from api import app
from bd.singelton import Singelton
from src.entities.fundacion import Fundacion
