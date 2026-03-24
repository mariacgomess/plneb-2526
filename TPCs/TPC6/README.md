# Analisador de Coocorrências de Personagens (Harry Potter)

## Objetivo do Código
Este script tem como objetivo identificar os amigos entre personagens no livro *Harry Potter e a Pedra Filosofal*, ou seja **identificar e contabilizar interações (coocorrências)**, . O programa assume que, se dois nomes de personagens aparecem na mesma frase, eles são amigos, ou seja existe uma relação de interação entre eles,.

---

### 1. Carregamento do Modelo e Corpus
O script utiliza a biblioteca **spaCy**, uma ferramenta avançada para Processamento de Linguagem Natural:
- **Modelo:** Carrega o modelo `pt_core_news_lg` (Português, Large), que possui vetores de palavras e maior precisão para Reconhecimento de Entidades Mencionadas (NER).
- **Leitura:** O ficheiro de texto é lido com codificação `utf-8` para garantir a correta interpretação de caracteres acentuados.

### 2. Segmentação e Reconhecimento de Entidades (NER)
O núcleo da análise baseia-se na estrutura do objeto `doc` gerado pelo spaCy:
- **Iteração por Frases:** O código percorre o texto frase a frase (`doc.sents`). Isto é crucial, pois define o "contexto" da interação.
- **Identificação de Personagens:** Dentro de cada frase, o script procura entidades com a etiqueta `PER` (Personas/Pessoas). 
- **Filtragem Única:** Para cada frase, é criada uma lista `amigo` que armazena os nomes encontrados, garantindo que não há repetições da mesma personagem na mesma frase (evitando auto-correlação redundante).

### 3. Lógica de Coocorrência
O script estabelece relações quando o comprimento da lista `amigo` é superior a 1 (ou seja, pelo menos duas personagens diferentes na mesma frase, pois se houver apenas um personagem naquela frase não será possivel identificar amigos dela nesta):
- **Permutação de Pares:** O código utiliza ciclos `for` aninhados para comparar cada personagem `w` com todas as outras personagens `w2` presentes na frase.
- **Condição de Diferença:** A relação só é contabilizada se `w != w2`, impedindo que uma personagem tenha uma relação consigo mesma.

### 4. Estrutura de Dados (Dicionário de Frequências)
Os resultados são armazenados num dicionário aninhado chamado `amigos`, seguindo esta lógica:
- **Chave Primária:** Nome da personagem A.
- **Chave Secundária:** Nome da personagem B.
- **Valor:** Inteiro que representa o número de vezes que A e B apareceram juntos numa frase.
- **Contagem Incremental:** Se o par já existir, o contador aumenta (`+= 1`); caso contrário, é inicializado.

### 5. Saída de Dados
O resultado final é impresso na consola, revelando um dicionário Python. Esta estrutura permite identificar:
- Quem são as personagens mais centrais da trama.
- A força da ligação entre pares específicos (ex: Harry e Ron vs. Harry e Neville).



