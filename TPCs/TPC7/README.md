# Home page para dicionário de conceitos

Este documento explica o funcionamento lógico da aplicação Flask e a interação entre os ficheiros de backend e os templates de frontend.

## Backend (`tpc7.py`)

O servidor utiliza a framework **Flask** para gerir as rotas e o motor de renderização **Jinja2**.

1.  **Carregamento de Dados:**
    - O ficheiro `dicionario_medico.json` é aberto no arranque e carregado para a variável global `db` como um dicionário Python.
2.  **Rotas Principais:**
    - `@app.get("/")`: Renderiza a página de entrada (`home.html`).
    - `@app.get("/conceitos")`: Extrai as chaves do dicionário (`db.keys()`), ordena-as alfabeticamente com `sorted()` e envia a lista para o template `conceitos.html`.
    - `@app.get("/api/")`: Funciona como um endpoint de dados puro, devolvendo o dicionário completo em formato JSON para integração com outros sistemas.
3.  **Configuração do Servidor:**
    - O servidor corre na porta `5002` com o `debug=True`, o que permite ver erros em tempo real e reiniciar automaticamente ao detetar alterações no código.

## Frontend (Templates)

A aplicação utiliza o conceito de **Herança de Templates** para evitar repetição de código.

* **`layout.html` (Base):** Contém a estrutura esqueleto (HTML5, Bootstrap, Navbar e Footer). Define blocos (`{% block %}`) onde o conteúdo específico de cada página será injetado.
* **`home.html` (Extensão):** Preenche o bloco principal com um "Jumbotron" de boas-vindas e cartões informativos sobre as funcionalidades.
* **`conceitos.html` (Dinâmico):** - Utiliza um ciclo `{% for c in conceitos %}` para iterar sobre a lista enviada pelo Python.
    - Gera automaticamente um item de lista para cada termo médico presente na base de dados.
    - Inclui uma lógica condicional `{% if not conceitos %}` para exibir uma mensagem de alerta caso a base de dados esteja vazia.

## Fluxo de Dados

1. O utilizador acede a uma URL.
2. O **Flask** processa o pedido e manipula os dados do JSON.
3. Os dados são injetados nos **Templates**.
4. O **Bootstrap** (via CDN no layout) aplica o estilo visual final antes de entregar a página ao navegador.