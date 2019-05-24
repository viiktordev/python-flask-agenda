from model.endereco import Endereco
class Contato():
    def __init__(self, id, nome, celular = '', telefone = '', email = '', endereco = ''):
        self.__id = id
        self.__nome = nome
        self.__celular = celular
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco

    @staticmethod
    def cria(tupla):
        try:
            id = tupla[0]
            nome = tupla[1]
            celular = tupla[2]
            telefone = tupla[3]
            email = tupla[4]
            endereco = Endereco.cria([
                '',
                tupla[5],
                tupla[6],
                tupla[7],
                tupla[8],
                tupla[9],
                tupla[10],
                tupla[11]
            ])
            return Contato(id, nome, celular, telefone, email, endereco)
        except Exception as e:
            print("problema ao criar CONTATO - Erro: " + e.__str__())
        


    def getAll(self):
        return({'id':self.__id,
            'nome':self.__nome,
            'celular':self.__celular,
            'telefone':self.__telefone,
            'email':self.__email,
            'endereco':self.__endereco})
            
    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getCelular(self):
        return self.__celular

    def getTelefone(self):
        return self.__telefone
    
    def getEmail(self):
        return self.__email
    
    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def __dict__(self):
        d = dict()
        d["id"] = self.__id
        d["nome"] = self.__nome
        d["celular"] = self.__celular
        d["telefone"] = self.__telefone
        d["email"] = self.__email
        d["endereco"] = self.__endereco.__dict__()
        return d