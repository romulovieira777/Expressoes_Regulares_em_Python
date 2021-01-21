# https://regex101.com/r/wjfSus/1/


# Importando biblioteca
import re


# Declarando uma variável
string = '''
Válidos
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-133215646589.6543215648978977
+1.11123123
-0.154987
1.121654987
10.123
10.1
-1.1
Inválidos
10..2
++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
'''


# Criando funções
def is_float(string):
    # Retorna o valor da string se for verdadeiro
    return bool(re.search(r'^[+-]?\d+(?:\.\d+)?$', string))


def is_int(string):
    # Retorna o valor da string se for verdadeiro
    return bool(re.search(r'^[+-]?\d+$', string))


# Criando uma estrutura de repetição utilizando while, declarando uma variável para usuário inserir os valores
while True:
    numero = input('Digite um número: ')

    # Verifica se o número foi convertido para inteiro
    if is_int(numero):
        # Declarando uma variável
        numero = int(numero)

        # Apresentando os valores na tela
        print(f'O número {numero} foi convertido para int')

        # Para continuar o bloco de execução
        continue

    # Verifica se o número foi convertido para float
    if is_float(numero):
        # Declarando uma variável
        numero = float(numero)

        # Apresentando os valores na tela
        print(f'O número {numero} foi convertido para float')

        # Para continuar o bloco de execução
        continue
