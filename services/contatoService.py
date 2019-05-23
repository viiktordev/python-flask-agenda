from dao.contatoDao import ContatoDao
def getAll():
    dao = ContatoDao()
    contatos = dao.getAll()
    print(contatos)