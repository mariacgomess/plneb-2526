
##(1)
## Objetivo

O código apresentado tem como objetivo demonstrar duas formas diferentes de inverter uma string em Python.

---

## Função `reverse1(s)`

A função `reverse1` inverte a **ordem das palavras** de uma frase.

- Divide a frase numa lista de palavras usando `split(" ")`.
- Percorre essa lista ao contrário com `reversed()`.
- Concatena as palavras numa nova string.
- Imprime o resultado final.

Exemplo:
Entrada: `A Maria toca guitarra`  
Saída: `guitarra toca Maria A`

---

## Função `reverse2(s)`

A função `reverse2` inverte **todos os caracteres** da string.

- Utiliza slicing (`s[::-1]`) para percorrer a string do fim para o início.
- Concatena cada caractere numa nova string.
- Imprime o resultado final.

Exemplo:
Entrada: `A Maria toca guitarra`  
Saída: `arratiug acot airaM A`

##(2)

## Objetivo

O código apresentado tem como objetivo contar o número de letras **"A"** (maiúsculas e minúsculas) existentes numa frase.

---

## Função `counta(s)`

A função `counta` recebe uma string como argumento e conta quantas vezes aparece a letra **"A"** ou **"a"**.

### Funcionamento

- Inicializa uma variável `n` com valor 0.
- Percorre cada caractere da string com um ciclo `for`.
- Verifica se o caractere é `"A"` ou `"a"`.
- Se for, incrementa o contador `n`.
- No final, imprime o número total de ocorrências.

### Exemplo

Entrada: `A Maria toca guitarra`  
Saída: `6`

--

##(3)

## Objetivo

O código apresentado tem como objetivo contar o número de **vogais** existentes numa frase.

---

## Função `vowels(s)`

A função `vowels` recebe uma string como argumento e conta quantas vogais (`a`, `e`, `i`, `o`, `u`) estão presentes.

### Funcionamento

- Inicializa a variável `n` com valor 0.
- Converte a string para minúsculas usando `lower()`, garantindo que letras maiúsculas também sejam consideradas.
- Percorre cada caractere da nova string com um ciclo `for`.
- Verifica se o caractere pertence à lista de vogais.
- Se pertencer, incrementa o contador `n`.
- No final, imprime o total de vogais encontradas.

### Exemplo

Entrada: `A Maria toca guitarra`  
Saída: `10`

--

##(4)

## Objetivo

O código apresentado tem como objetivo converter uma frase para **letras minúsculas**.

---

## Função `lower(s)`

A função `lower` recebe uma string como argumento e transforma todos os seus caracteres em minúsculas.

### Funcionamento

- Utiliza o método `lower()` para converter a string para minúsculas.
- Armazena o resultado na variável `ns`.
- Imprime a nova string convertida.

### Exemplo

Entrada: `A Maria toca guitarra`  
Saída: `a maria toca guitarra`

--

##(5)

## Objetivo

O código apresentado tem como objetivo converter uma frase para **letras maiúsculas**.

---

## Função `upper(s)`

A função `upper` recebe uma string como argumento e transforma todos os seus caracteres em maiúsculas.

### Funcionamento

- Utiliza o método `upper()` para converter a string para maiúsculas.
- Armazena o resultado na variável `ns`.
- Imprime a nova string convertida.

### Exemplo

Entrada: `A Maria toca guitarra`  
Saída: `A MARIA TOCA GUITARRA`

--

##(6)

## Objetivo

O código apresentado tem como objetivo verificar se uma palavra ou expressão é uma **capicua**, ou seja, se pode ser lida da mesma forma da esquerda para a direita e vice-versa.

---

## Função `reverse2(s)`

Esta função recebe uma string e devolve a string invertida. (Criada e explicada anterirormente)

## Função `capicua(s)`

Esta função verifica se a string é uma capicua.

### Funcionamento

- Converte a string para minúsculas com `lower()`.
- Compara a string original (já em minúsculas) com a sua versão invertida (criada através da função reverse2(s)).
- Se forem iguais, a variável `capicua` passa a `True`.
- Imprime o resultado (`True` ou `False`).

---

## Exemplos

- `Ana` → `True`  
- `Maria` → `False`  
- `20:02` → `True`  

--

##(7)

## Objetivo

O código apresentado tem como objetivo verificar se **todas as letras** de uma string (`s1`) existem noutra string (`s2`).

---

## Função `balanc(s1, s2)`

A função `balanc` recebe duas strings como argumentos e verifica se todos os caracteres de `s1` estão presentes em `s2`.

### Funcionamento

- Inicializa a variável `b` com o valor `True`.
- Percorre cada caractere da string `s1`.
- Para cada letra, verifica se ela **não** pertence a `s2`.
- Se encontrar uma letra que não exista em `s2`, a variável `b` passa a `False`.
- No final, imprime o valor lógico (`True` ou `False`).

---

## Exemplos

- `balanc("erro","torre")` → `True`  
- `balanc("torre","erro")` → `False`  

Isto acontece porque todas as letras de cada palavra existem na outra.

---

##(8)

## Objetivo

O código apresentado tem como objetivo contar quantas vezes uma sequência de caracteres (`s1`) aparece dentro de outra string (`s2`), sem contar sobreposições.

---

## Função `ocr(s1, s2)`

A função `ocr` recebe duas strings como argumentos e percorre `s2` para encontrar ocorrências de `s1`.

### Funcionamento

- Calcula o comprimento da string a procurar (`ls1`).
- Inicializa o contador de ocorrências `c` a `0`.
- Utiliza um ciclo `while` para percorrer a string `s2`.
- A cada passo, verifica se a fatia de `s2` (do índice atual `i` até `i + ls1`) é igual a `s1`.
- Se for igual:
    - Incrementa o contador `c`.
    - Avança o índice `i` pelo comprimento de `s1` (para evitar contar a mesma parte da string novamente).
- Se não for igual:
    - Avança o índice `i` apenas uma unidade.
- No final, imprime o número total de ocorrências encontradas.

---

## Exemplos

- `ocr("na","bananas")` → `2`

Isto acontece porque a sílaba "na" ocorre duas vezes na palavra "bananas" e o algoritmo conta ambas corretamente neste caso.

---

##(9)

## Objetivo

O código apresentado tem como objetivo verificar se duas palavras são **anagramas**, ou seja, se possuem **as mesmas letras**, mas possivelmente em ordem diferente.

---

## Função `anagrama(s1, s2)`

A função recebe duas strings (`s1` e `s2`) e verifica se ambas contêm exatamente as mesmas letras.

### Funcionamento

- Inicializa a variável `b` com o valor `True`.
- Percorre cada letra de `s1` e verifica se **não** existe em `s2`. Se encontrar, define `b = False`.
- Percorre cada letra de `s2` e verifica se **não** existe em `s1`. Se encontrar, define `b = False`.
- No final, imprime o resultado (`True` ou `False`).

---

## Exemplos

- `anagrama("listen","silent")` → `True`  
- `anagrama("hello","world")` → `False`  

Isto acontece porque todas as letras de "listen", estão presentes em "silent" e vice-versa, o que não se verifica com "hello" e "world"

---