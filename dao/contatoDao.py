from database.database import Database
import sqlite3

class ContatoDao():

    def insere(self, contato):
        conn = Database().conexao()
        cur = conn.cursor()
        sql = 'INSERT INTO contato (nome, celular, telefone, email, endereco)\
             values(?,?,?,?,?)'
        cur.execute(sql, (contato.getNome, contato.getCelular,
        contato.getTelefone, contato.getEmail, 1))
