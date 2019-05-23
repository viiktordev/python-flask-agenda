from flask import Flask, jsonify, render_template, redirect, request, url_for
import requests
import json

app = Flask(__name__)

apiAgenda = 'http://localhost:5000/'
apiCep = 'http://localhost:5002/'

@app.route('/', methods=['GET', 'POST'])
def contatos():
    r = requests.get(apiAgenda+'contato')
    msg = ""
    if 'msg' in request.args:
        msg = request.args["msg"]

    data = json.loads(r.text)

    return render_template('contatos.html', contatos = data, msg = msg)

@app.route('/criar', methods=['GET'])
def criarContato():

    return render_template('criar.html')

@app.route('/editar/<int:id>', methods=['GET'])
def editarContato(id):
    r = requests.get(apiAgenda+'contato')
    
    data = json.loads(r.text)
    print(data[0])
    return render_template('editar.html', contato=data[0])

@app.route('/salvar', methods=['POST'])
def salvar():
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
    
    return redirect(url_for('contatos', msg = "succ"))

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
    r = requests.get(apiCep+'endereco/'+cep)

    data = json.loads(r.text)

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=5001)