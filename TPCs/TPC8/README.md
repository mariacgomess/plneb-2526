# Dicionário Médico — Aplicação Web com Flask

## Objetivo do Código
Este projeto tem como objetivo disponibilizar um **dicionário de terminologia médica** através de uma aplicação web local, desenvolvida com o framework **Flask** (Python). A aplicação permite consultar, **pesquisar**, adicionar e eliminar conceitos médicos de forma interativa, com base num ficheiro JSON que serve de base de dados.


### 1. Base de Dados

O ficheiro `dicionario_medico.json` é carregado no arranque da aplicação e mantido em memória durante a execução:
- **Estrutura:** dicionário simples `{ "designação": "descrição", ... }`
- **Persistência:** sempre que um conceito é adicionado ou eliminado, o ficheiro JSON é reescrito para guardar as alterações
- **Codificação:** o ficheiro é lido com `encoding='latin-1'` para garantir a correta interpretação de caracteres especiais

### 2. Motor de Pesquisa

O núcleo mais relevante da aplicação é a funcionalidade de pesquisa, acessível em `/pesquisar`. O utilizador pode configurar três comportamentos distintos através de checkboxes:

#### 2.1 Pesquisa por Substring (comportamento padrão)
- Procura o termo introduzido como parte de qualquer palavra
- Exemplo: pesquisar `"dor"` encontra `"doença"`, `"dores"`, `"ardor"`
- Implementado com o operador `in` do Python sobre strings

#### 2.2 Palavra Exata (`word_boundary`)
- Ativa quando o utilizador marca a opção **"Palavra exata"**
- O texto é dividido em palavras individuais (`.split()`), com limpeza prévia de pontuação (`.`, `,`, `;`)
- Só há correspondência se o termo pesquisado for igual a uma das palavras isoladas
- Exemplo: `"dor"` **não** encontra `"doença"`, mas encontra `"dor"` isolada

#### 2.3 Sensibilidade a Maiúsculas (`case_sensitive`)
- Por defeito, a pesquisa é insensível a maiúsculas (tudo convertido para minúsculas antes de comparar)
- Com a opção **"Maiúsculas/minúsculas"** ativa, a comparação é feita com o texto original
- Exemplo: com a opção ativa, `"Dor"` **não** encontra `"dor"`

#### 2.4 Destaque a Negrito
- Após encontrar uma correspondência, a palavra pesquisada é destacada a **negrito** no resultado
- Em modo insensível a maiúsculas, utiliza `re.compile` com a flag `re.IGNORECASE` para substituir a ocorrência mantendo o texto original
- O HTML gerado (`<b>palavra</b>`) é passado ao template com o filtro `|safe` do Jinja2

---

### 3. Templates HTML (Jinja2)

Os templates utilizam o sistema de herança do **Jinja2**:
- `base.html` define a estrutura comum (cabeçalho, navegação, estilos, rodapé)
- Todos os outros templates estendem `base.html` com `{% extends "base.html" %}`
- O conteúdo específico de cada página é inserido no bloco `{% block content %}`

