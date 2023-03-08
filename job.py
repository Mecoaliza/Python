
import csv
import sqlite3

# Criar um novo banco de dados

conn = sqlite3.connect('dsadb.db')

# Criar uma tabela para armazenar os dados 
conn.execute('''CREATE TABLE producao (
                produto TEXT,
                quantidade INTEGER,
                preco_medio REAL,
                receita_total REAL

)''')

# Grava e fecha a conexão

conn.commit()
conn.close()

# Abre o arquivo csv 

with open('producao_alimentos.csv','r') as file:
 
#  Cria um leitor do CSV

reader = csv.reader(file)

# Pula a primeira linha do cabeçalho

next(reader)

# Conecta com o banco de dados 

conn = sqlite3.connect('dsadb.db')

# Inseri cada linha do arquivo na tabela do banco de dados

for row in reader:
    conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?,?,?,?)', row)

conn.commit()
conn.close()

print("Job Concluído com Sucesso!")



