from flask import Flask, jsonify, Blueprint, request
from contatoApi import contatoApp

app = Flask(__name__)
app.register_blueprint(contatoApp)

@app.route('/')
def listarAll():
    return jsonify({'teste':'ok'})

if __name__ == '__main__':
    app.run(host='localhost',port=5000)