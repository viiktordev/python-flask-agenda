from database.database import Database
import sqlite3

class EnderecoDao():

    def insere(self, endereco):
        aux = 0
        try:
            conn = Database().conexao()
            cur = conn.cursor()
            sql = 'INSERT INTO endereco (cep, logradouro, bairro, numero, complemento, uf)\
                values(?,?,?,?,?,?)'
            cur.execute(sql, ( endereco.cep,
                endereco.logradouro, endereco.bairro, endereco.numero, endereco.complemento, endereco.uf ))
            
            conn.commit()
            aux = cur.lastrowid
        except Exception as e:
            print("Erro ao inserir CONTATO - "+e.__str__())
        finally:
            cur.close()
            conn.close()

        return aux
