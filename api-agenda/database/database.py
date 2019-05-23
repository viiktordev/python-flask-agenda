import sqlite3
class Database():

    def cria(self):

        conn = self.conexao()
        cur = conn.cursor()
        cur.execute ("create table if not exists endereco \
            (id integer PRIMARY KEY, \
            cep text not null,\
            logradouro text,\
            bairro text,\
            numero text,\
            complemento text,\
            localidade text,\
            uf text);")
        
        cur.execute ("create table if not exists contato \
            (id integer PRIMARY KEY AUTOINCREMENT, \
            nome text not null,\
            celular text,\
            telefone text,\
            email text,\
            idEndereco integer,\
            FOREIGN KEY (idEndereco) REFERENCES endereco(id));")
                
        conn.close()

    def conexao(self):
        conn = sqlite3.connect('agenda')

        return conn