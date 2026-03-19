from django.test import TestCase
import requests

cep = "58037665"

url = f'http://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url)

dados = resposta.json()

print(dados)