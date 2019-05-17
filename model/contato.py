class Contato():
    def __init__(self, nome, celular = '', telefone = '', email = '', endereco = ''):
        self.__nome = nome
        self.__celular = celular
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco

    def getAll(self):
        return({'nome':self.__nome,
            'celular':self.__celular,
            'telefone':self.__telefone,
            'email':self.__email,
            'endereco':self.__endereco})
            
    def getNome(self):
        return self.nome

    def getCelular(self):
        return self.celular

    def getTelefone(self):
        return self.telefone
    
    def getEmail(self):
        return self.email
    
    def getEndereco(self):
        return self.endereco