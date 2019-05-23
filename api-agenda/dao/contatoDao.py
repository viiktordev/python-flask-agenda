from database.database import Database
import sqlite3

class ContatoDao():
    @staticmethod
    def getAll():
        try:
            conn = Database().conexao()
            cur = conn.cursor()
            sql = "SELECT contato.id, contato.nome, contato.celular,\
                contato.telefone, contato.email, endereco.cep, endereco.logradouro,\
                endereco.bairro, endereco.numero, endereco.complemento, endereco.localidade,\
                endereco.uf \
                FROM contato INNER JOIN endereco ON\
                contato.idEndereco = endereco.id"
            cur.execute(sql)
            rows = cur.fetchall()
            return rows
        except Exception as e:
            print("Erro ao consultar todos - "+e.__str__())
        finally:
            cur.close()
            conn.close()

    def insere(self, contato):
        try:
            conn = Database().conexao()
            cur = conn.cursor()
            sql = "INSERT INTO contato (nome, celular, telefone, email, idEndereco)\
                values(?, ?, ?, ?, ?)"
            cur.execute(sql, (contato.getNome(), contato.getCelular(),
                contato.getTelefone(), contato.getEmail(), contato.getEndereco()))

            print(cur.lastrowid)
            conn.commit()
        except Exception as e:
            print("Erro ao inserir- "+e.__str__())
        finally:
            
            cur.close()
            conn.close()

