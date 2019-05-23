from database.database import Database
import sqlite3

class EnderecoDao():

    def insere(self, endereco):
        
        try:
            conn = Database().conexao()
            cur = conn.cursor()
            sql = 'INSERT INTO endereco (idContato, cep, logradouro, bairro, numero, complemento, uf)\
                values(?,?,?,?,?,?,?)'
            cur.execute(sql, (endereco.idContato, endereco.cep,
                endereco.logradouro, endereco.bairro, endereco.numero, endereco.complemento, endereco.uf ))
            
            aux = cur.lastrowid
            conn.commit()
        except Exception as e:
            print("Erro ao inserir CONTATO - "+e.__str__())
        finally:
            cur.close()
            conn.close()

        return aux
