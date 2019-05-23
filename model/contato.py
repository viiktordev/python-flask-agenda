class Contato():
    def __init__(self, id, nome, celular = '', telefone = '', email = '', endereco = ''):
        self.__id = id
        self.__nome = nome
        self.__celular = celular
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco

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

    def __dict__(self):
        d = ditc()
        d["id"] = self.__id
        d["nome"] = self.__nome
        d["celular"] = self.__celular
        d["telefone"] = self.__telefone
        d["email"] = self.__email
        d["endereco"] = self.__endereco
        return d