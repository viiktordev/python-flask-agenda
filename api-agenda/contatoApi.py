from flask import Flask, jsonify, Blueprint, request
from services.contatoService import getAll as service_listar, insere

app = Flask(__name__)

contatoApp = Blueprint('contatoApp', __name__, template_folder='templates')

@contatoApp.route('/contato', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(lista)

@contatoApp.route('/contato', mothods=['POST'])
def cadastrar():
    try:
        contato = request.get_json()
        insere(contato)
        return jsonify(service_listar())
    except expression as identifier:
        return ({'mensagem':'algo de errado não está certo'})
    