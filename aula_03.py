# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+


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

print(re.findall(r'jo+ão', text, flags=re.IGNORECASE))  # Escolhendo João e incluindo o utilizando + e ignorando as
# letras tanto maiúscula como minúscula

print(re.sub(r'jo+ão', 'Felicty', text, flags=re.IGNORECASE))  # Substituindo João e trocando pelo nome de Felicty
# incluindo o utilizando +  e ignorando as letras tanto maiúscula como minúscula

print(re.sub(r'jo*ão*', 'Felicty', text, flags=re.IGNORECASE))  # Substituindo João e trocando pelo nome de Felicty
# incluindo o utilizando +  e ignorando as letras tanto maiúscula como minúscula

print(re.sub(r'jo?ão*', 'Felicty', text, flags=re.I))  # Substituindo João e trocando pelo nome de Felicty
# incluindo o utilizando +  e ignorando as letras tanto maiúscula como minúscula

print(re.findall(r'jo{1,}ão{1,}', text, flags=re.I))  # Encontrando João e incluindo o utilizando +  e ignorando
# as letras tanto maiúscula como minúscula

print(re.findall(r'Come{3}e{1,2}', text, flags=re.I))  # Encontrando a palavra vem no texto e ignorando as letras
# tanto maiúscula como minúscula

print(re.findall(r'j[o]+ão+', text, flags=re.I))  # Encontrando a palavra joão no texto e ignorando as letras
# tanto maiúscula como minúscula


# Declarando uma variável
text_02 = 'John loves to be loved'

# Apresentando na tela do usuário
print(re.findall(r'lov[ed]{0,2}', text_02, flags=re.I))  # Encontrando a palavra love e loved no texto e ignorando
# as letras anto maiúscula como minúscula.
