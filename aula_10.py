# 0.0.0.0 255.255.255.255
# 025.258.963-10 02525896310

# Teste essa expressão
# em https://regex101.com/r/lWVPOr/1


# Importando bibliotecas
import re


# Declarando duas variáveis
cpf = '025.258.963-10'


cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', flags=0)
print(cpf_reg_exp.search(cpf))


# Declarando uma variável
ip_reg_exp = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$')


# Criando uma estrutura de repetição utilizando o for
for i in range(301):
    # Gerando números de ip e declarando uma variável
    ip = f'{i}.{i}.{i}.{i}'

    # Apresentando os valores na tela
    print(ip, ip_reg_exp.findall(ip))
