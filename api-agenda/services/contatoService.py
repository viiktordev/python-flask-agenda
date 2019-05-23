from model.contato import Contato
from dao.contatoDao import ContatoDao

def getAll():
    dao = ContatoDao()
    conatosDB = dao.getAll()
    listaContato = []
    for dadosContato in conatosDB:
        listaContato.append(Contato.cria(dadosContato).__dict__())

    return listaContato

def insere():
    dao = ContatoDao()
    