
import csv
import sqlite3

# Criar um novo banco de dados

conn = sqlite3.connect('dsabd.bd')

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