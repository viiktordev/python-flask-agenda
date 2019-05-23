import requests as req

def buscaEndereco(cep):
    url = "https://viacep.com.br/ws/{}/json/".format(cep)
    retorno = req.get(url).json()
    d = dict()
    if('erro' in retorno):
        return {'erro':True}
        
    d["bairro"] = retorno["bairro"]
    d["localidade"] = retorno["localidade"]
    d["uf"] = retorno["uf"]
    d["logradouro"] = retorno["logradouro"]
    return d
