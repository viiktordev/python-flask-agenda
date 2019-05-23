from flask import Flask, jsonify, render_template, redirect, request, url_for
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contatos():

    r = requests.get('http://localhost:5000/contato')
    
    data = json.loads(r.text)

    print(data)
    '''
    if 'ctt' in request.args:
        lol = json.loads(request.args['ctt'])
        cont.append(lol)
    '''
    return render_template('contatos.html', contatos = data)

@app.route('/criar', methods=['GET'])
def criarContato():

    return render_template('criar.html')

@app.route('/editar/<int:id>', methods=['GET'])
def editarContato(id):

    r = requests.get('http://localhost:5000/contato')
    
    data = json.loads(r.text)
    print(data[0])
    return render_template('editar.html', contato=data[0])


@app.route('/editar', methods=['POST'])
def editar():
    nome = request.form['nome']
    numero = request.form['numero']
    email = request.form['email']
    celular = request.form['celular']
    #endereco
    cep = request.form['cep']
    bairro = request.form['bairro']
    complemento = request.form['complemento']
    localidade = request.form['localidade']
    logradouro = request.form['logradouro']
    uf = request.form['uf']

    return jsonify("teste")

@app.route('/buscarCEP', methods=['POST'])
def buscarCEP():
    cep = request.form['cep']

    print(cep)
    return jsonify("{ success: true, cep: {cep} }")

if __name__ == '__main__':
    app.run(host='localhost', port=5001)