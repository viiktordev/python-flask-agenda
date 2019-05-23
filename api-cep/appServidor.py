from flask import Flask, jsonify, Blueprint, request
from enderecoApi import enderecoApp

app = Flask(__name__)
app.register_blueprint(enderecoApp)

@app.route('/')
def ok():
    return jsonify({'mensagem':'tudo pronto'})

if __name__ == '__main__':
    app.run(host='localhost',port=5002)