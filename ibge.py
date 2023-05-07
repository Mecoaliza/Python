
import requests

link = "https://servicodados.ibge.gov.br/api/v3/agregados/7392/periodos/-6/variaveis/10484?localidades=N1[all]"

requisicao = requests.get(link)
informacoes = requisicao.json()

import pprint
pprint.pprint(informacoes[0])

#def get_link():
    #response = get(link).json()
    #return response[link]
item_busca = informacoes[0]['variavel'] #Só a variável do dicionario
resultados = informacoes[0]['resultados'][0]['series'] #Só a série do dicionario

print(item_busca)
print(resultados)