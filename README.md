# Expressões Regulares em Python
### Curso de Expressões Regulares em Python na Udemy 
#### :computer: Temas abordados durante o curso foram :rocket:
- [Seção 01 - Introdução]()


Link para o curso 100% Gratuito: [Udemy](https://www.udemy.com/course/expressoes-regulares-com-python-3-curso-gratuito/)


### :computer: Comandos em Python que foram usados nos Arquivos acima: :rocket:
**O que faz a função ascii:**

Seleciona as palavras com e sem acento.

**Sintaxe**

~~~py
flags=re.ASCII
~~~

**Exemplo**

~~~py
print(re.findall(r'\S+', text, flags=re.ASCII))
~~~

**O que faz a função bool:**

Converter qualquer valor para um booleano, se o valor puder ser interpretado como um valor verdade ou falso.

**Sintaxe**

~~~py
bool(<variável>)
~~~

**Exemplo**

~~~py
 return bool(re.search(r'^[+-]?\d+$', string))
~~~

**O que faz a função compile:**

Copia um texto especificado.

**Sintaxe**

~~~py
re.compile(r<texto>)
~~~

**Exemplo**

~~~py
regexp = re.compile(r'test')
~~~

**O que faz a função continue:**

Interrompe a execução do ciclo sem interromper a execução do laço de repetição.

**Sintaxe**

~~~py
continue
~~~

**Exemplo**

~~~py
while True:
    numero = input('Digite um número: ')
    if is_int(numero):        
        numero = int(numero)
        print(f'O número {numero} foi convertido para int')
        continue

~~~

**O que faz a função def:**

É para definir uma função que é uma sequência de comandos que executa alguma tarefa e que tem um nome.

**Sintaxe**

~~~py
def nome(<parâmetros>):
    comandos:
~~~

**Exemplo**

~~~py
def hello(meu_nome):
    print('Olá',meu_nome)
~~~

**O que faz a função dotall:**

Seleciona as palavras independente se tem quebra de linhas.

**Sintaxe**

~~~py
flags=re.DOTALL
~~~

**Exemplo**

~~~py
print(re.findall(r'^t.*d$', text_02, flags=re.I | re.DOTALL))
~~~

**O que faz a função findall:**

Encontra todas as ocorrências da palavra procurada no texto.

**Sintaxe**

~~~py
findall(r<variável>, <texto>)
~~~

**Exemplo**

~~~py
print(re.findall(r'test', string))
~~~

**O que faz a função float:**

Devolve um número de ponto flutuante construído a partir de um número ou string.

**Sintaxe**

~~~py
float(<variável>)
~~~

**Exemplo**

~~~py
nota1 = float(input("Entre com a primeira nota: "))
~~~

**O que faz a função for:**

Executa um ciclo para cada elemento do objeto que está sendo iterado.

**Sintaxe**

~~~py
for <variável> in <objeto iterável>:
    bloco de instrução
~~~

**Exemplo**

~~~py
for numero in range(1, 6):
    print(numero)
~~~

**O que faz a função if:**

É uma estrutura de condição que permite avaliar uma expressão e, de acordo com seu resultado, executar uma determinada ação.

**Sintaxe**

~~~py
if(<variável>)
~~~

**Exemplo**

~~~py
idade = 18
if idade < 20:
    print('Você é jovem!')
~~~

**O que faz a função ignorecase:**

Ignora a os caracteres tanto maiúscula como minúscula.

**Sintaxe**

~~~py
flags=re.IGNORECASE
~~~

**Exemplo**

~~~py
print(re.findall(r'jOãO|mAriA', text, flags=re.IGNORECASE))
~~~

**O que faz a função import:**

É uma linha com o caminho completo para o arquivo python que contem o módulo que se deseja importar.

**Sintaxe**

~~~py
import <biblioteca>
~~~

**Exemplo**

~~~py
import re
~~~

**O que faz a função in:**

Verifica se o operando a sua esquerda, está contido na lista a sua direita.

**Sintaxe**

~~~py
 in (<variável>)
~~~

**Exemplo**

~~~py
2 and 3 in range(1,6)
~~~

**O que faz a função input:**

É para entrada de dados feita pelo usuário.

**Sintaxe**

~~~py
input(<variável>)
~~~

**Exemplo**

~~~py
nome = input('Entre com o nome do aluno: ')
~~~

**O que a faz função print:**

Imprimir um argumento passado na tela.

**Sintaxe**

~~~py
print(<variável>)
~~~

**Exemplo**

~~~py
print('Olá, Mundo!')
~~~

**O que a faz função pprint:**

Imprimir um argumento passado na tela.

**Sintaxe**

~~~py
pprint(<variável>)
~~~

**Exemplo**

~~~py
pprint(tags)
~~~

**O que a função range faz:**

Permite-nos especificar o início da sequência, o passo, e o valor final.

**Sintaxe**

~~~py
range(<variável>):
~~~

**Exemplo**

~~~py
range(0, 10)
~~~

**O que a função return faz:**

É utilizada para declarar a informação a ser retornada pela função.

**Sintaxe**

~~~py
return(<condição>):
~~~

**Exemplo**

~~~py
def soma(x,y):
    num = x * y
    return num
~~~

**O que faz a função search:**

Encontra a primeira ocorrência da palavra procurada no texto.

**Sintaxe**

~~~py
search(r<variável>, <texto>)
~~~

**Exemplo**

~~~py
print(re.search(r'test', string))
~~~

**O que faz a função sub:**

Substitui a palavra que deseja no texto especificado.

**Sintaxe**

~~~py
sub(r<variável>, <texto>, <string>)
~~~

**Exemplo**

~~~py
print(re.sub(r'test', 'ABCD', string))
~~~

**O que a função while faz:**

Repete a sequência de comandos definida em seu corpo enquanto a <condição> permanece verdadeira.

**Sintaxe**

~~~py
while(<condição>):
~~~

**Exemplo**

~~~py
numero = 1
while numero < 6:
    print(numero)
    numero += 1
~~~














