from database.database import Database
from model.contato import Contato
from dao.contatoDao import ContatoDao
from model.endereco import Endereco
from services.contatoService import getAll

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
getAll()


#end = Endereco(contato)

#print(end.contato.getAll())