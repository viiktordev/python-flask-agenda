class Endereco():
    def __init__(self, id, cep='', logradouro='', bairro='', numero='', complemento='', localidade='', uf=''):
        self.id = id
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.numero = numero
        self.complemento = complemento
        self.localidade = localidade
        self.uf = uf

    def setId(self, id):
        self.__id = id

    def getIdContato(self):
        return self.__idContato

    @staticmethod
    def cria(tupla):
        try:
            id = tupla[0]
            cep = tupla[1]
            logradouro = tupla[2]
            bairro = tupla[3]
            numero = tupla[4]
            complemento = tupla[5]
            localidade = tupla[6]
            uf = tupla[7]
            return Endereco(id, cep, logradouro, bairro, numero, complemento, localidade, uf)
        except Exception as e:
            print("problema ao criar ENDERECO - Erro: " + e.__str__())

    
    def __dict__(self):
        d = dict()
        d["id"] = self.__id
        d["cep"] = self.__cep
        d["logradouro"] = self.__logradouro
        d["bairro"] = self.__bairro
        d["numero"] = self.__numero
        d["complemento"] = self.__complemento
        d["localidade"] = self.__localidade
        d["uf"] = self.__uf
        return d

    