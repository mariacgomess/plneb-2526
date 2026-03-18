# TPC5
## Objetivo do Código
Este script tem como objetivo **extrair automaticamente todas as doenças de A a Z** de um site, incluindo:

- Nome da doença
- Descrição curta (listagem)
- Descrição completa (página individual da doença)

O resultado final é guardado num ficheiro JSON (`doencas.json`).

---

### 1. Normalização e Limpeza de URLs
Diferente de uma abordagem de extração direta de links, o script utiliza a função `limpar_doenca(palavra)`. Esta função prepara o nome da doença para ser injetado num URL estático:
- Converte o texto para minúsculas e substitui espaços por hífens;
- Utiliza a biblioteca `unicodedata` para remover acentos (normalização NFD);
- Codifica em ASCII ignorando caracteres especiais para garantir que o slug do URL (`/content/nome-da-doenca`) seja válido.

### 2. Função extrair_pagina
Esta função é o núcleo do scraper e processa cada letra do abecedário:
- **Extração da Listagem:** Localiza os blocos `views-row` e extrai a designação (através do caminho `div.div.h3.a`) e a descrição curta (`views-field-body`).
- **Navegação Dinâmica:** Em vez de extrair o `href`, o script reconstrói o URL de detalhe concatenando a base `/content/` com o nome da doença já limpo.
- **Lógica de Extração de Texto:** Acede à página de detalhe e procura a `div` com a classe `field-name-body`.

### 3. Filtro de Conteúdo Detalhado
O script implementa uma lógica seletiva para a descrição completa (`fdescricao`):
- Percorre os elementos filhos de field-item even, usamos .children ao invés do método anteriormente usado (.get_text()) por razões estruturais, pois permite isolar cada nó individualmente e interromper a extração ao encontrar um h2, evitando o colapso de todo o texto num único bloco indiferenciado.
- **Interrupção Estratégica:** O ciclo `for` é interrompido ao encontrar a primeira tag `h2`. Isto é feito para recolher apenas a introdução ou o resumo inicial da página de detalhe, ignorando secções posteriores como sintomas ou tratamentos que costumam estar sob cabeçalhos `h2`.
- Trata tanto elementos com tags (usando `get_text`) como texto solto (NavigableStrings).

### 4. Iteração e Agregação
- O script utiliza `string.ascii_lowercase` para navegar de 'a' a 'z'.
- Utiliza o operador de união de dicionários (`|`) introduzido nas versões recentes do Python para fundir os resultados de cada página no dicionário principal `res`, permitindo aceder às páginas de cada letra com todas a doenças, aplicando a função extrair_pagina a cada página.

### 5. Estrutura de Dados (JSON)
O ficheiro final `doencas.json` organiza a informação com a seguinte hierarquia:
- **Chave:** Nome original da doença.
- **Valor:** Um objeto com os campos:
    - `short`: Descrição breve retirada da página de índice.
    - `full`: Texto extraído da introdução da página de detalhe.

---

### Resumo do funcionamento do Script

1. **Ciclo Alfabético:** Itera sobre as letras de A a Z para construir os URLs das listas.
2. **Parsing da Lista:** Para cada doença na lista, guarda o nome e a descrição curta.
3. **Limpeza de String:** Transforma o nome da doença num formato compatível com URLs (sem acentos, minúsculas e hífens).
4. **Extração Seletiva:** Acede à página específica e extrai o texto até encontrar o primeiro cabeçalho `h2`, ficando apenas com a descrição longa
5. **Persistência:** Guarda o dicionário resultante num ficheiro JSON com codificação UTF-8 e indentação para facilitar a leitura humana.