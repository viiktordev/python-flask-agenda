from flask import Flask, jsonify, request, Blueprint
from services.cepService import buscaEndereco 

app = Flask(__name__)

enderecoApp = Blueprint('enderecoApp', __name__)

@enderecoApp.route('/endereco/<string:cep>', methods=['GET'])
def getEndereco(cep):
    if(len(cep)!= 8):
        return jsonify({'error':'formato de cep invalido'}),400

    endereco = buscaEndereco(cep)
    if('erro' in endereco):
        return jsonify({'error':'cep invalido'})
    return jsonify(endereco)