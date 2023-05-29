# API -> É um lugar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo: Criar uma api de consulta, criação, edição e explisão de livros
# 2. URL Base: localhost
# 3. Endpoints: Quais as funcionalidades que vou disponibilizar?
  # - localhost/livros (GET)
    #- localhost/livros (POST)
  # - localhost/livros/id (GET)
# - localhost/livros/id (PUT)
 #- localhost/livros/id (DELETE)
# Esse é o endereço que a pessoa tem que digitar, para ir
# 4. Quais recursos? - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Pense em Python',
        'autor': 'Allen B.Downey',
        'status': 'lendo'
    },
    {
        'id': 2,
        'título': 'Tenho sérios poemas mentais',
        'autor': 'Pedro Salomão',
        'status': 'lido'  
    }

]

# Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)
# Constultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for i in livros:
        if livros.get('id') == id:
            return jsonify(livros)
# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)        
# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
        
        return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)