from flask import Flask, jsonify, render_template, redirect, request, url_for
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contatos():
    '''
    r = requests.get('http://localhost:5000/')
    cont = json.loads(r.text)

    if 'ctt' in request.args:
        lol = json.loads(request.args['ctt'])
        cont.append(lol)
    '''
    return render_template('contatos.html')

@app.route('/criar', methods=['GET'])
def criarContato():

    return render_template('criar.html')

@app.route('/editar/<int:id>', methods=['GET'])
def editarContato(id):

    return render_template('editar.html', id=id)


@app.route('/salvar', methods=['POST'])
def salvar():
    contato = {'Nome': request.form['Nome'], 'Numero': request.form['Numero']}
    c = jsonify(contato)
    return redirect(url_for('.contatos', ctt=c.data))

if __name__ == '__main__':
    app.run(host='localhost', port=5001)