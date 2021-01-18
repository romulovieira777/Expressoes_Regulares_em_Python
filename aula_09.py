# Importando bibliotecas
import re
from pprint import pprint


# Declarando uma variável
text = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# Apresentando os valores na tela
print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))  # Econtrando somente o IP no texto

pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))  # Econtrando somente o IP no texto

pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)', text))  # Econtrando o IP e o texto ativo e inativo
# no texto

# Positive lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', text))  # Econtrando o IP e o texto active

# Negative lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', text))  # Econtrando o IP e o texto inactive

pprint(re.findall(r'.+', text))  # Econtrando todas as palavras e números no texto

# Negative lookahead
pprint(re.findall(r'(?=.*inactive).+', text))  # Econtrando o IP e o texto inactive

# Positive lookahead
pprint(re.findall(r'(?=.*[^in]active).+', text))  # Econtrando o IP e o texto active

# Positive lookbehind
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))  # Encontrando no texto online

# Positive loohbehind
pprint(re.findall(r'\w+(?<=OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))  # Encontrando no texto offline

# Negative loohbehind
pprint(re.findall(r'\w+(?<!OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))  # Encontrando no texto online
