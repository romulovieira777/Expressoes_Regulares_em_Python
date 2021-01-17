# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]
# \b -> borda
# \B -> não borda


# Importando uma biblioteca
import re


# Declarando uma variável
text = '''
João brought    flowers to his beloved girlfriend on January 10, 1970,
Maria was her name.


It was an excellent year in the life of joão. He had 5 children, all of whom are currently adults.
maria, now his wife, still makes that coffee with cheese bread in the afternoons of
Sunday. Also right! Being the good miner she is, she never forgets her famous
cheese bread.
I can't get enough of listening to Maria:
"Joooooooooãooooooo, the coffee is ready here. Comeeess"!
'''

# Apresentando os valores na tela
print(re.findall(r'[a-z]', text))  # Encontrando todas as letras de a à z, as palavras minúsculas com exeção das
# maiúcula e palavras acentuadas

print(re.findall(r'[a-z]+', text))  # Encontrando todas as palavras de a à z, as palavras minúsculas com exeção das
# maiúscula e palavras acentuadas

print(re.findall(r'[a-z]+', text, flags=re.I))  # Encontrando todas as palavras de a à z, as palavras minúsculas
# com exeção das palavras acentuadas

print(re.findall(r'[a-zA-Z]+', text))  # Encontrando todas as palavras de a à z, com exeção das palavras acentuadas

print(re.findall(r'[a-zA-Z0-9]+', text))  # Encontrando todas as palavras de a à z e os números, com exeção das
# palavras acentuadas

print(re.findall(r'[a-zA-Z0-9À-ú]+', text))  # Encontrando todas as palavras de a à z

print(re.findall(r'\w+', text))  # Encontrando todas as palavras de a à z

print(re.findall(r'\w', text))  # Encontrando todas as letras de a à z

print(re.findall(r'\w+', text, flags=re.ASCII))  # Encontrando todas as palavras de a à z, com exeção das
# palavras acentuadas

print(re.findall(r'\W', text))  # Encontrando todos os pontos, vírgulas, quebra de linha etc

print(re.findall(r'\W', text, flags=re.ASCII))  # Encontrando todos os pontos, vírgulas, quebra de linha e palavras
# acentuadas

print(re.findall(r'\d+', text))  # Encontrando todos os números

print(re.findall(r'\D+', text, flags=re.ASCII))  # Encontrando tudo menos os números

print(re.findall(r'\s+', text, flags=re.ASCII))  # Encontrando as quebra de linhas e os espaços no texto

print(re.findall(r'\S+', text, flags=re.ASCII))  # Encontrando tudo que não for espaço no texto

print(re.findall(r'\bflow\w+', text, flags=re.I))  # Encontrando a palavra flower

print(re.findall(r'\be\w+', text, flags=re.I))  # Encontrando todas as palavras que começa com a letra e

print(re.findall(r'\w+e\b', text, flags=re.I))  # Encontrando todas as palavras que tenham a letra e

print(re.findall(r'\b\w{4}\b', text, flags=re.I))  # Encontrando todas as palavras que tenham quatro letras

print(re.findall(r'\w{4}', text, flags=re.I))  # Encontrando todas as palavras que tenham quatro letras e as que tem
# mais letras ele corta

print(re.findall(r'flowe\B', text, flags=re.I))  # Encontrando a palavra sem olhar a borda
