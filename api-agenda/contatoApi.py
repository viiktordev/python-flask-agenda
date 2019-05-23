from flask import Flask, jsonify, Blueprint, request
from services.contatoService import getAll as service_listar

app = Flask(__name__)

contatoApp = Blueprint('contatoApp', __name__, template_folder='templates')

@contatoApp.route('/contato', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(lista)