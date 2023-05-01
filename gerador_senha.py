import random
import string   #importar funções com numeros e letras

def password_generator(Len_pass = 8):
    ascii_options = string.ascii_letters   # Essa linha cria uma variável que recebe todas as letras do alfabeto (maiúsculas e minúsculas) em formato ASCII. 
    number_options = string.digits         #Essa linha cria uma variável que recebe todos os dígitos numéricos em formato de string (ou seja, como texto).
    options = ascii_options + number_options  #Concatenar todas as opções

    password_user = ""

    for i in range(0, Len_pass):   #Esse range cria um array com 8 digitos, o I é apenas uma variável auxiliar 
        digit = random.choice(options)
        password_user = password_user + digit
    
    return password_user

user_choice = input("Quantos digitos na senha?")

if user_choice.isdigit():
    user_choice = int(user_choice)
else:
    print("Entrada inválida!")
    quit()

response = password_generator(Len_pass = user_choice)
print(f"Senha gerada:\n{response}")