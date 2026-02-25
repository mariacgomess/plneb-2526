# Ficha_RE_1 – Expressões Regulares em Python

---

# Exercício 1

## 1.1

### Objetivo  
Dada uma linha de texto, definir um programa que determina se a palavra **"hello"** aparece no início da linha.

### Explicação  
A função `re.match()` verifica se o padrão ocorre exatamente no início da string.

- Se a linha começar por `"hello"`, devolve um objeto `Match`.
- Caso contrário, devolve `None`.


### Resultados  
Entrada: print(re.match(r'hello',line1)) 
Saída:'<re.Match object; span=(0, 5), match='hello'>'

Entrada: print(re.match(r'hello',line2)) 
Saída:None

Entrada:print(re.match(r'hello',line3)) 
Saída:None


---

## 1.2

### Objetivo  
Dada uma linha de texto, definir um programa que determina se a palavra **"hello"** aparece em qualquer posição da linha.

### Explicação  
A função `re.search()` procura o padrão ao longo de toda a string.

- Se encontrar `"hello"` em qualquer posição, devolve um objeto `Match`.
- Caso contrário, devolve `None`.

Usamos esta função em vez do `re.match()` porque esta procura em toda a frase enquanto que o `re.match()` apenas verifica se está no ínicio da string.

### Resultados  
Entrada:print(re.search(r'hello',line1))
Saida:<re.Match object; span=(0, 5), match='hello'>

Entrada:print(re.search(r'hello',line2))
Saida:None

Entrada:print(re.search(r'hello',line3))
Saida:<re.Match object; span=(4, 9), match='hello'>

---

## 1.3

### Objetivo  
Dada uma linha de texto, determinar todas as ocorrências da palavra **"hello"**.

### Explicação  
A função `re.findall()` devolve uma lista com todas as correspondências encontradas, usando a flag `re.IGNORECASE`, a pesquisa não distingue maiúsculas de minúsculas deveolvendo-nos o pretendido.

### Resultados  
Entrada:line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
Saida:['Hello', 'hello', 'hello', 'HELLO']


---

## 1.4

### Objetivo  
Dada uma linha de texto, substituir todas as ocorrências da palavra **"hello"** por outra expressão.

### Explicação  
A função `re.sub()` permite substituir todas as ocorrências do padrão indicado por uma nova string.

Recebe o padrão a procurar e a string de substituição, substituindo o padrão pedido pela nova string.

### Resultados  
Entrada:"Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
Saida:*YEP* there! Uh, hi, *YEP*, it's me... Heyyy, *YEP*? *YEP*!

---

## 1.5

### Objetivo  
Dada uma linha de texto, dividir a frase utilizando um determinado separador.

### Explicação  
A função `re.split()` divide a string sempre que encontra o padrão indicado, respondendo ao nosso objetivo.

### Resultados  
Entrada:line = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."
Saida:['bananas', ' laranjas', ' maçãs', ' uvas', ' melancias', ' cerejas', ' kiwis', ' etc.']


---

# Exercício 2

### Objetivo  
Definir uma função que verifica se uma frase termina com a expressão **"por favor"** seguida de `.`, `!` ou `?`.

### Explicação  
A função utiliza uma expressão regular que:

- Procura a expressão `"por favor"`.
- Garante que termina com um dos sinais de pontuação indicados.
- Usa o símbolo `$` para assegurar que está no final da frase.

Se cumprir o padrão, a condição é considerada verdadeira.

### Resultados  
Entrada:print(palavra_magica("Posso ir à casa de banho, por favor?"))
Saida:<re.Match object; span=(26, 36), match='por favor?'>

Entrada:print(palavra_magica("Preciso de um favor."))
Saida:None

---

# Exercício 3

### Objetivo  
Definir uma função que conta o número de vezes que a palavra **"eu"** aparece numa linha de texto.

### Explicação  
A função utiliza `re.findall()` com a flag `IGNORECASE` para:

- Encontrar todas as ocorrências de `"eu"` e coloca-as numa lista.
- Contar o número de elementos na lista, ou seja o número de vezes que a palavra eu foi encontrada.


### Resultados 
Entrada:print(narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."))
Saida:6

---

# Exercício 4

### Objetivo  
Definir uma função que substitui todas as ocorrências de `"LEI"` por outro curso indicado pelo utilizador.

### Explicação  
A função utiliza `re.sub()` para:

- Localizar todas as ocorrências da palavra `"LEI"`.
- Substituí-las pelo novo curso fornecido como argumento.

### Resultados
Entrada:print(troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.",'ENGBIOM'))
Saida:ENGBIOM é o melhor curso! Adoro ENGBIOM! Gostar de ENGBIOM devia ser uma lei.

---

# Exercício 5

### Objetivo  
Definir uma função que calcula a soma de números inteiros presentes numa string separados por vírgulas.

### Explicação  
A função:

1. Divide a string usando `re.split()`.
2. Converte cada elemento em inteiro.
3. Soma todos os valores.
4. Devolve o resultado final.

### Resultados
Entrada:print(soma_string("4,-6,2,3,8,-3,0,2,-5,1"))
Saida:6

---

# Exercício 6

### Objetivo  
Definir uma função que identifica determinados pronomes pessoais numa frase.

### Explicação  
A expressão regular procura pronomes como:

- ele
- ela
- eu
- tu
- nós

Utiliza alternativas (`|`) e a flag `IGNORECASE`.

A função devolve uma lista com os pronomes encontrados.

### Resultados
Entrada: print(pronomes('Eu e Ela foramos passear ao rio. Ela tropeçou e caiu e eu gritei: ELA, TU ESTÁS BEM? Ela disse que sim e nós continuamos a passear'))
Saida:['Eu', 'Ela', 'Ela', 'eu', 'ELA', 'TU', 'Ela', 'nós']
---

# Exercício 7

### Objetivo  
Definir uma função que verifica se uma string corresponde a um nome de variável válido.

### Explicação  
A expressão regular garante que:

- Começa por uma letra.
- Pode conter letras, números ou `_`.
- Não contém espaços nem caracteres inválidos.
- Termina corretamente (`$`).

A função devolve `True` ou `False`, caso corresponda ou não aos requisitos.

### Resultados
Entrada:print(variavel_valida('m23_WN'))
Saida:True

Entrada:print(variavel_valida('123_WN'))
Saida:False

Entrada:print(variavel_valida('m23_*WN'))
Saida:False
---

# Exercício 8

### Objetivo  
Definir uma função que extrai todos os números inteiros (positivos ou negativos) de uma frase.

### Explicação  
A expressão regular utilizada permite:

- Um sinal negativo opcional (`-?`).
- Um ou mais dígitos (`\d+`).

A função devolve uma lista com todos os números encontrados, que correspondam a estes requisitos.

### Resultados
Entrada:print(inteiros('Hoje dia 29 de fevereiro de 2026 registamos uma temperatura de -3 graus'))
Saida:['21', '2026', '-3']

---

# Exercício 9

### Objetivo  
Definir uma função que substitui espaços numa string por underscores (`_`).

### Explicação  
A expressão `\s+` identifica um ou mais espaços consecutivos.

Todos os espaços são substituídos por `_` usando `re.sub()`.

### Resultados
Entrada:print(underscores('Hoje dia 29 de  fevereiro de 2026 registamos uma temperatura de -3 graus'))
Saida:Hoje_dia_29_de_fevereiro_de_2026_registamos_uma_temperatura_de_-3_graus
---

# Exercício 10

### Objetivo  
Definir uma função que separa códigos postais no formato `"XXXX-XXX"` nas suas duas partes.

### Explicação  
A função utiliza `re.split()` com o hífen (`-`) como separador.

Divide o código postal em:

- Parte inicial (4 dígitos)
- Parte final (3 dígitos)

Devolve essas duas partes numa lista, que é depois adicionada a uma lista com todos os pares.

### Resultados
Entrada:print(codigos_postais(lista))
Saida:[['4700', '000'], ['1234', '567'], ['8541', '543'], ['4123', '974'], ['9481', '025']]