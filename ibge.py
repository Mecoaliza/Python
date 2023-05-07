
import requests

link = "https://api.splink.org.br/datasets/format/json"

def get_link():
    response = get(link).json()
    return response[link]


#requisicao = requests.get(link)
#informacoes = requisicao.json()

#import pprint
#pprint.pprint()

#item_busca = informacoes[0]['variavel'] #Só a variável
#resultados = informacoes[0]['resultados'][0]['series'] #Só a série

#print(item_busca)
#print(resultados)