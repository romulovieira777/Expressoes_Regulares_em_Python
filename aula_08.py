# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall \n


# Importando uma biblioteca
import re


# Declarando uma variável
text = '''
131.768.460-53
055.123.060-50
955.123.060-90
'''

# Apresentando os valores na tela
print(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', text))  # Encontrando todos os cpfs no texto

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', text, flags=re.MULTILINE))  # Encontrando todos os cpfs no texto


# Declarando uma variável
text_02 = 'The John Likes revelry And loves to be loved'

# Apresentando os valores na tela
print(re.findall(r'^t.*d$', text_02, flags=re.I))  # Encontrando a frase inteira que começa com T e termina com D

print(re.findall(r'^t.*d$', text_02, flags=re.I | re.DOTALL))  # Encontrando a frase inteira que começa com T e termina
# com D
