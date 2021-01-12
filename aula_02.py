# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres


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
print(re.findall('João|Maria', text))  # Escolhendo João ou Maria utilizando o pipe |

print(re.findall(r'João|Maria|ad..ts', text))  # Escolhendo João ou Maria utilizando o pipe | e o ponto pode ser
# qualquer letra em seu lugar

print(re.findall(r'João|joão|Maria', text))  # Escolhendo João ou Maria utilizando o pipe |

print(re.findall(r'[Jj]João|joão|[Mm]aria', text))  # Escolhendo João ou Maria utilizando o pipe | e o conjunto
# de caracteres []

print(re.findall(r'[a-z]aria', text))  # Escolhendo Maria utilizando o pipe | e o conjunto de caracteres []

print(re.findall(r'[a-zA-Z]aria', text))  # Escolhendo Maria utilizando o pipe | e o conjunto de caracteres []

print(re.findall(r'[a-zA-Z0-9]aria', text))  # Escolhendo Maria utilizando o pipe | e o conjunto de caracteres []

print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', text))  # Escolhendo João e Maria utilizando o pipe | e o conjunto
# de caracteres []

print(re.findall(r'jOãO|mAriA', text, flags=re.I))  # Escolhendo João e Maria utilizando o pipe | e ignora as letras
# tanto maiúscula quanto minúscula
