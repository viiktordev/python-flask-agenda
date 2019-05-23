from database.database import Database
from model.contato import Contato
from dao.contatoDao import ContatoDao
from model.endereco import Endereco
from services.contatoService import getAll, insere

dao = ContatoDao()

contato = Contato('victor','123','456','teste@teste',1)


#print(contato.getAll())
'''
try:
    conn = Database().conexao()

    cur = conn.cursor()
    
    cur.execute("insert into endereco\
        (cep, logradouro, bairro, numero, complemento, localidade, uf)\
        values(?,?,?,?,?,?,?)",('07124000','rua 777', 'bairro 1', '77', 'casa 7', 'sao paulo', 'SP'))
    
    cur.execute("INSERT INTO contato (nome, celular, telefone, email, idEndereco)\
                values('victor', '123', '456', 'vitor@vitor',55)")
    
    
    conn.commit()
    cur.close()
    conn.close()
except Exception as e:
    print(e)
    '''

#print(contato.getNome())
#dao.insere(contato)
#insere({'teste': 1, 'teste2': 2})

contatoDados = dict()
contatoDados['nome'] = "vitor"
contatoDados['celular'] = "132456"
contatoDados['telefone'] = "987654"
contatoDados['email'] = "vitor@giganti"
contatoDados['cep'] = "07124000"
contatoDados['logradouro'] = "rua teste"
contatoDados['bairro'] = "bairro teste"
contatoDados['numero'] = "10"
contatoDados['complemento'] = "casa 2"
contatoDados['localidade'] = "Sao Paulo"
contatoDados['uf'] = "SP"

insere(contatoDados)


#end = Endereco(contato)

#print(end.contato.getAll())