# NER em Português com BERT — Reconhecimento de Entidades Nomeadas

## Objetivo do Código

Este projeto tem como objetivo preparar um pipeline de **Reconhecimento de Entidades Nomeadas (NER)** em português, utilizando o modelo pré-treinado **BERTimbau** (`neuralmind/bert-base-portuguese-cased`) como base. O notebook cobre as etapas de carregamento de dados, tokenização com alinhamento de etiquetas, e preparação do modelo para fine-tuning numa tarefa de classificação de tokens.

---

## Estrutura do Notebook

### 1. Data Loading

O dataset utilizado é o `lfcc/portuguese_ner`, carregado diretamente do Hugging Face Hub:

```python
from datasets import load_dataset
dataset_raw = load_dataset("lfcc/portuguese_ner")
```

**Output:**
```
DatasetDict({
    train: Dataset({ features: ['tokens', 'ner_tags'], num_rows: 3716 })
    test:  Dataset({ features: ['tokens', 'ner_tags'], num_rows: 930  })
})
```

O dataset está dividido em **3716 exemplos de treino** e **930 de teste**. Cada exemplo é composto por uma lista de tokens (`tokens`) e as respetivas etiquetas NER (`ner_tags`).

**Classes de entidades disponíveis:**

| Etiqueta | Significado |
|---|---|
| `O` | Fora de entidade |
| `B-Data` / `I-Data` | Data (início / interior) |
| `B-Local` / `I-Local` | Local |
| `B-Organizacao` / `I-Organizacao` | Organização |
| `B-Pessoa` / `I-Pessoa` | Pessoa |
| `B-Profissao` / `I-Profissao` | Profissão |

O esquema de etiquetagem segue o formato **BIO** (Begin, Inside, Outside), standard em tarefas de NER.

---

### 2. Data Pre-Processing

#### 2.1 Tokenizador

É utilizado o tokenizador correspondente ao modelo BERTimbau:

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
```

A escolha de usar o tokenizador do mesmo modelo que será usado para treino é fundamental — garante que os IDs de tokens são consistentes com os embeddings aprendidos durante o pré-treino.

#### 2.2 O Problema da Sub-tokenização

O BERT usa um tokenizador **WordPiece**, que divide palavras desconhecidas em sub-tokens. Por exemplo:

```
Input:  ["as", "aulas", "plneb", "são", "interessantes", "!"]
Output: ['[CLS]', 'as', 'aulas', 'pl', '##ne', '##b', 'são', 'interessantes', '!', '[SEP]']
```

A palavra `plneb` foi dividida em 3 sub-tokens (`pl`, `##ne`, `##b`). Isto cria um desfasamento entre o número de tokens originais (6) e o número de tokens do BERT (10), o que impossibilita a atribuição direta das etiquetas NER.

O método `word_ids()` devolve o mapeamento entre cada token BERT e a palavra original de onde veio:

```python
inputs.word_ids()
# [None, 0, 1, 2, 2, 2, 3, 4, 5, None]
```

Os `None` correspondem aos tokens especiais `[CLS]` e `[SEP]`.

#### 2.3 Alinhamento de Etiquetas

Para resolver o desfasamento, é implementada a função `align_labels_with_tokens`:

```python
def align_labels_with_tokens(word_ids, labels):
    new_labels = []
    previous_word = None
    for word_id in word_ids:
        if word_id == None:
            new_labels.append(-100)       # tokens especiais: ignorar
        elif previous_word != word_id:
            new_labels.append(labels[word_id])  # primeiro sub-token: manter etiqueta
        else:
            new_labels.append(-100)       # sub-tokens seguintes: ignorar
        previous_word = word_id
    return new_labels
```

A lógica é a seguinte: apenas o **primeiro sub-token** de cada palavra recebe a etiqueta original; os restantes sub-tokens e os tokens especiais recebem `-100`, que é o valor que o PyTorch usa para ignorar posições no cálculo da loss durante o treino.

#### 2.4 Tokenização do Dataset Completo

A função `tokenize_dataset` aplica a tokenização e o alinhamento a todos os exemplos:

```python
train_data = tokenize_dataset(dataset_raw["train"]) 
test_data  = tokenize_dataset(dataset_raw["test"])    
```

Os datasets resultantes têm 4 colunas: `input_ids`, `token_type_ids`, `attention_mask` e `labels`.

---

### 3. Carregamento do Modelo

```python
from transformers import AutoModelForTokenClassification
model = AutoModelForTokenClassification.from_pretrained("neuralmind/bert-base-portuguese-cased")
```

O modelo BERTimbau é carregado com uma **cabeça de classificação de tokens** (`BertForTokenClassification`), adequada para tarefas NER. Como o modelo pré-treinado foi originalmente treinado para Masked Language Modeling (MLM), os pesos da cabeça de classificação (`classifier.weight` e `classifier.bias`) são **inicializados aleatoriamente** — são os únicos pesos que precisam de ser treinados do zero. Os restantes pesos do BERT são herdados do pré-treino e serão apenas afinados (fine-tuned).

O relatório de carregamento mostra também pesos `UNEXPECTED` (pertencentes à cabeça MLM original, que são descartados) e pesos `MISSING` (a nova cabeça de classificação, que é inicializada aleatoriamente), o que é o comportamento esperado neste tipo de transferência de aprendizagem.

---

## Notas sobre a Pipeline

O notebook cobre as etapas de preparação até ao carregamento do modelo, estando pronto para a fase de fine-tuning. Os passos seguintes seriam:

1. Definir as métricas de avaliação (tipicamente F1-score por entidade)
2. Configurar o `Trainer` da biblioteca `transformers` com os hiperparâmetros de treino
3. Treinar o modelo no `train_dataset` e avaliar no `test_dataset`
