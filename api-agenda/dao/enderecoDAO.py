from database.database import Database
import sqlite3

class EnderecoDao():

    def insere(self, endereco):
        conn = Database().conexao()
        cur = conn.cursor()
        sql = 'INSERT INTO endereco (idContato, cep, logradouro, bairro, numero, complemento, uf)\
             values(?,?,?,?,?,?,?)'
        cur.execute(sql, (contato.getNome, contato.getCelular,
        contato.getTelefone, contato.getEmail, 1))

