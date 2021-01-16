# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3


# Importando uma biblioteca
import re
from pprint import pprint


# Declarando uma variável
text = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

# Apresentando o valor na tela
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', text))  # Encontrando o p e o div

print(re.findall(r'<([dpiv]{1,3})>.+?<\/\1>', text))  # Encontrando o p e o div

print(re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', text))  # Encontrando o p e o div

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1" \3" \4', text))


# Declarando uma variável
tags = re.sub(r'(<([dpiv]{1,3})>.+?<\/\2>)', text)

# Apresentando o valor na tela
print(tags)
pprint(tags)

# Criando uma estrutura de repetição utilizando o for
for tag in tags:
    # Apresentando o valor na tela
    print(tag)

# Criando uma estrutura de repetição utilizando o for
for tag in tags:
    # Criando duas variáveis para acessar o grupo
    one, two = tag
    # Apresentando o valor na tela
    print(one, two)


# Declarando uma variável
tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', text)

# Criando uma estrutura de repetição utilizando o for
for tag in tags:
    # Criando duas variáveis para acessar o grupo
    one, two, three = tag
    # Apresentando o valor na tela
    print(three)


# Declarando uma variável
tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', text)

# Apresentando o valor na tela
pprint(tags)


# Declarando uma variável
tags = re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', text)

# Apresentando o valor na tela
pprint(tags)


# Declarando uma variável
cpf = '147.852.963-12'

# Apresentando o valor na tela
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))  # Encontrando o cpf

print(re.findall(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}', cpf))  # Encontrando o cpf

print(re.findall(r'(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))  # Encontrando o cpf

print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))  # Encontrando o cpf


# Declarando uma variável
tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/\1>', text)

# Apresentando o valor na tela
pprint(tags)


# Declarando uma variável
tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', text)

# Apresentando o valor na tela
pprint(tags)
