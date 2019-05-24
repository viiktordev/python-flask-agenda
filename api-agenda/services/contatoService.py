from model.contato import Contato
from dao.contatoDao import ContatoDao
from dao.enderecoDAO import EnderecoDao

def getAll():
    dao = ContatoDao()
    conatosDB = dao.getAll()
    listaContato = []
    for dadosContato in conatosDB:
        listaContato.append(Contato.cria(dadosContato).__dict__())

    return listaContato

def insere(contatoDados):
    dao = ContatoDao()
    enderecoDao = EnderecoDao()

    listaContato = [
        '',
        contatoDados['nome'],
        contatoDados['celular'],
        contatoDados['telefone'],
        contatoDados['email'],
        contatoDados['cep'],
        contatoDados['logradouro'],
        contatoDados['bairro'],
        contatoDados['numero'],
        contatoDados['complemento'],
        contatoDados['localidade'],
        contatoDados['uf']
    ]
    
    contato = Contato.cria(listaContato)
    endereco = contato.getEndereco()

    idEndereco = enderecoDao.insere(endereco)

    contato.setEndereco(idEndereco)

    print(dao.insere(contato))

    #endereco.setId(idContato)

    #idEndereco = enderecoDao.insere(endereco)

    #dao.updateIdEndereco(endereco,idEndereco)


    #print(contato.__dict__())

    
    