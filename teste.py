from database.database import Database
from model.contato import Contato
from dao.contatoDao import ContatoDao
from model.endereco import Endereco

db = Database()

db.cria()
'''
contato = Contato('victor')

print(contato.getAll())'''

try:
    conn = Database().conexao()

    cur = conn.cursor()
    cur.execute("insert into endereco\
        (cep, logradouro, bairro, numero, complemento, localidade, uf)\
        values(?,?,?,?,?,?,?)",('777','rua 777', 'bairro', '77', 'casa 7', 'sao paulo', 'SP'))
    
    conn.commit()
    cur.close()
    conn.close()
except Exception as e:
    print(e)

end = Endereco('07124000', )