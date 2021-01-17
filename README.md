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
















