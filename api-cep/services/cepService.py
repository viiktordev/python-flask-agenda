import requests as req

def buscaEndereco(cep):
    url = "https://viacep.com.br/ws/{}/json/".format(cep)
    retorno = req.get(url).json()
    d = dict(retorno)
    return d

print(buscaEndereco('07124000'))