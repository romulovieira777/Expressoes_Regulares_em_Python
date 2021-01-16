# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação


# Importando uma biblioteca
import re


# Declarando uma variável
cpf = '147.852.963-12'

# Apresentando o valor na tela
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))  # Encontrando o cpf

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))  # Encontrando o cpf

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))  # Encontrando o cpf

print(re.findall(r'[^a-z]+', cpf))  # Encontrando caracteres na variável

print(re.findall(r'[^0-9]+', cpf))  # Encontrando o cpf

print(re.findall(r'[^0-9a-zA-Z.]+', cpf))  # Encontrando o cpf
