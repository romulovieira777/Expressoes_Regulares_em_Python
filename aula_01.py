# Deixando os links para consultar a biblioteca do Python oficial
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html

# Importando uma biblioteca
import re

# Declarando uma variável
string = 'This is a test of regulars expressions'

# Apesentando os valores na tela
print(re.search(r'test', string))  # Search encontra a primeira ocorrência

print(re.findall(r'test', string))  # Findall Encontra todas as ocorrências

print(re.sub(r'test', 'ABCD', string))  # Substitui a palavra test para ABCD

# Declarando uma variável
regexp = re.compile(r'test')

# Apresentando os valores na tela
print(regexp.search(string))

print(regexp.findall(string))

print(regexp.sub('DEF', string))
