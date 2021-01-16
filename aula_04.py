# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1


# Importando uma biblioteca
import re


# Declarando uma variável
text = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

# Apresentando o valor na tela
print(re.findall(r'<[dpiv]{1,3}>', text))  # Encontrando o p e o div

print(re.findall(r'<[dpiv]{1,3}>.*', text))  # Encontrando o p e o div

print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', text))  # Encontrando o p e o div

print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', text))  # Encontrando o p e o div

print(re.findall(r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>', text))  # Encontrando o p e o div

print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', text))  # Encontrando o p e o div
