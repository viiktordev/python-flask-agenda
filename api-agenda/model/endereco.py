class Endereco():
    def __init__(self, idContato, cep='', logradouro='', bairro='', numero='', complemento='', localidade='', uf=''):
        self.__idContato = idContato
        self.__cep = cep
        self.__logradouro = logradouro
        self.__bairro = bairro
        self.__numero = numero
        self.__complemento = complemento
        self.__localidade = localidade
        self.__uf = uf

    def setId(self, idCont):
        self.__idContato = idCont

    def getIdContato(self):
        return self.__idContato

    @staticmethod
    def cria(tupla):
        try:
            idContato = tupla[0]
            cep = tupla[1]
            logradouro = tupla[2]
            bairro = tupla[3]
            numero = tupla[4]
            complemento = tupla[5]
            localidade = tupla[6]
            uf = tupla[7]
            return Endereco(idContato, cep, logradouro, bairro, numero, complemento, localidade, uf)
        except Exception as e:
            print("problema ao criar ENDERECO - Erro: " + e.__str__())

    
    def __dict__(self):
        d = dict()
        d["id"] = self.__idContato
        d["cep"] = self.__cep
        d["logradouro"] = self.__logradouro
        d["bairro"] = self.__bairro
        d["numero"] = self.__numero
        d["complemento"] = self.__complemento
        d["localidade"] = self.__localidade
        d["uf"] = self.__uf
        return d

    