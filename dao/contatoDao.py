from database.database import Database
import sqlite3

class ContatoDao():

    def insere(self, contato):
        try:
            conn = Database().conexao()
            cur = conn.cursor()
            sql = "INSERT INTO contato (nome, celular, telefone, email, idEndereco)\
                values(?, ?, ?, ?, ?)"
            cur.execute(sql, (contato.getNome(), contato.getCelular(),
            contato.getTelefone(), contato.getEmail(), 75))

            print(cur.lastrowid)
            conn.commit()
        except Exception as e:
            print("Erro - "+e.__str__())
        finally:
            
            cur.close()
            conn.close()

