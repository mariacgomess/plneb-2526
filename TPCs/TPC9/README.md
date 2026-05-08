# Word2Vec com Harry Potter — Embeddings de Palavras em Português

## Objetivo do Código

Este projeto tem como objetivo treinar e explorar modelos de **Word2Vec** sobre textos literários em português, utilizando os dois primeiros livros da saga *Harry Potter* como corpus. A experiência permite observar como diferentes configurações do modelo afetam a qualidade semântica dos embeddings gerados, testando relações de similaridade entre personagens e casas de Hogwarts.

---

## Preparação dos Dados

### 1. Corpus Utilizado

O corpus é composto por dois ficheiros de texto em português:

- `Harry_Potter_e_A_Pedra_Filosofal.txt`
- `Harry_Potter_Camara_Secreta-br.txt`

Ambos os ficheiros são lidos com codificação `utf8`. Juntos formam um corpus literário rico, com vocabulário consistente e personagens recorrentes, ideal para avaliar relações semânticas.

### 2. Pré-processamento

O pré-processamento é feito com o modelo de linguagem `pt_core_news_sm` do **spaCy**, aplicado a cada documento:

1. **Remoção de quebras de página** — o caractere `\f` é eliminado com `re.sub`
2. **Segmentação em frases** — o spaCy divide o texto em frases (`doc.sents`)
3. **Tokenização e limpeza** — para cada frase, os tokens são convertidos para minúsculas, excluindo pontuação e espaços em branco

O resultado é uma lista de listas de tokens (`sentences`), que serve diretamente como entrada para o treino do Word2Vec.

---

## Testes Realizados

Em cada variante do modelo são avaliadas as seguintes métricas:

- **`most_similar("harry")`** — os 10 termos semanticamente mais próximos de *harry*
- **Similaridade entre pares** — valores de cosseno entre *harry* e: `rony`, `hermione`, `sonserina`, `grifinória`
- **Aritmética vetorial** — `harry + sonserina − draco` para identificar qual personagem/conceito emerge da operação analógica

---

## Comparação de Configurações e Resultados

### Modelo Base — CBOW, vector_size=100, window=5, epochs=5

```python
Word2Vec(sentences, vector_size=100, window=5, min_count=2, sg=0, epochs=5, workers=3)
```

**`most_similar("harry")`**
| Palavra | Similaridade |
|---|---|
| hermione | 0.9951 |
| voz | 0.9910 |
| rony | 0.9903 |
| olhando | 0.9877 |
| cara | 0.9866 |
| hagrid | 0.9864 |
| olhou | 0.9862 |
| quando | 0.9858 |
| abriu | 0.9855 |
| viu | 0.9847 |

**Similaridade entre pares:**
| Par | Valor |
|---|---|
| harry ↔ rony | 0.9903 |
| harry ↔ hermione | 0.9951 |
| harry ↔ sonserina | 0.9693 |
| harry ↔ grifinória | 0.9594 |

**Aritmética vetorial** (`harry + sonserina − draco`): `hermione` (0.9945)

Os valores de similaridade são extremamente altos (próximos de 1.0) para todos os pares, o que indica que o modelo não está a diferenciar bem as palavras — tudo parece semanticamente próximo de tudo. O `most_similar` devolve maioritariamente verbos de ação genéricos (`olhou`, `abriu`, `viu`) e não personagens ou conceitos relevantes. A aritmética vetorial identifica *hermione* como resultado de `harry + sonserina − draco`, o que faz anão faz sentido narrativo.

---

### Alteração 1 — Aumento do `vector_size` para 200

```python
Word2Vec(sentences, vector_size=200, window=5, min_count=2, sg=0, epochs=5, workers=3)
```

| Parâmetro | Antes | Depois |
|---|---|---|
| `vector_size` | 100 | **200** |
| `window` | 5 | 5 |
| `epochs` | 5 | 5 |
| `sg` | 0 (CBOW) | 0 (CBOW) |

**`most_similar("harry")`**
| Palavra | Similaridade |
|---|---|
| hermione | 0.9977 |
| voz | 0.9974 |
| quando | 0.9955 |
| perguntou | 0.9954 |
| rony | 0.9954 |
| cara | 0.9941 |
| olhou | 0.9938 |
| mione | 0.9938 |
| rispidez | 0.9936 |
| viu | 0.9935 |

**Similaridade entre pares:**
| Par | Modelo Base | vector_size=200 | Variação |
|---|---|---|---|
| harry ↔ rony | 0.9903 | 0.9954 | ↑ +0.0051 |
| harry ↔ hermione | 0.9951 | 0.9977 | ↑ +0.0026 |
| harry ↔ sonserina | 0.9693 | 0.9874 | ↑ +0.0181 |
| harry ↔ grifinória | 0.9594 | 0.9839 | ↑ +0.0245 |

**Aritmética vetorial** (`harry + sonserina − draco`): `mão` (0.9978)

O aumento do `vector_size` fez subir todos os valores de similaridade, mas de forma indiscriminada — o problema de "tudo é parecido com tudo" agravou-se. O `most_similar` continua a devolver palavras genéricas, e aparece até `rispidez`, que claramente não é relevante. A aritmética vetorial piorou, devolvendo `mão` em vez de um personagem. Mais dimensões com poucas épocas não ajudaram o modelo a aprender representações mais significativas.

---

### Alteração 2 — Aumento do `window` para 8 e `epochs` para 30

```python
Word2Vec(sentences, vector_size=200, window=8, min_count=2, sg=0, epochs=30, workers=3)
```

| Parâmetro | Antes | Depois |
|---|---|---|
| `vector_size` | 200 | 200 |
| `window` | 5 | **8** |
| `epochs` | 5 | **30** |
| `sg` | 0 (CBOW) | 0 (CBOW) |

**`most_similar("harry")`**
| Palavra | Similaridade |
|---|---|
| ele | 0.5045 |
| mione | 0.4746 |
| neville | 0.4694 |
| portão | 0.4653 |
| dobby | 0.4449 |
| presidente | 0.4448 |
| simas | 0.4424 |
| riddle | 0.4317 |
| escapar | 0.4314 |
| colin | 0.4250 |

**Similaridade entre pares:**
| Par | Alter. 1 | Alter. 2 | Variação |
|---|---|---|---|
| harry ↔ rony | 0.9954 | 0.3005 | ↓ −0.6949 |
| harry ↔ hermione | 0.9977 | 0.2711 | ↓ −0.7266 |
| harry ↔ sonserina | 0.9874 | −0.0196 | ↓ −1.0070 |
| harry ↔ grifinória | 0.9839 | 0.1325 | ↓ −0.8514 |

**Aritmética vetorial** (`harry + sonserina − draco`): `grifinória` (0.6076)

Esta foi a alteração mais drástica. Os valores de similaridade caíram para níveis muito mais realistas (0.27–0.50), o que indica que o modelo passou a distinguir as palavras umas das outras em vez de comprimir tudo para valores próximos de 1. O `most_similar` melhorou significativamente: surgem personagens reais como `neville`, `dobby`, `riddle` e `colin`, que têm efetivamente ligação narrativa a *harry*. O resultado mais interessante é a aritmética vetorial — `harry + sonserina − draco` devolveu `grifinória` (0.6076), o que faz todo o sentido: se tirarmos o representante de Sonserina e adicionarmos a casa rival, o modelo aponta para a casa de Harry. Este é o resultado semanticamente mais coerente de todos os modelos testados.

---

### Alteração 3 — Mudança para Skip-gram (`sg=1`)

```python
Word2Vec(sentences, vector_size=200, window=8, min_count=2, sg=1, epochs=30, workers=3)
```

| Parâmetro | Antes | Depois |
|---|---|---|
| `vector_size` | 200 | 200 |
| `window` | 8 | 8 |
| `epochs` | 30 | 30 |
| `sg` | 0 (CBOW) | **1 (Skip-gram)** |

**`most_similar("casa")`**
| Palavra | Similaridade |
|---|---|
| receberá | 0.4663 |
| deveres | 0.4535 |
| acreditou | 0.4266 |
| honra | 0.4208 |
| assistindo | 0.4179 |
| espionando | 0.4136 |
| liguem | 0.4126 |
| estiverem | 0.4114 |
| majorca | 0.4105 |
| seriamente | 0.4082 |

**`most_similar("harry")`**
| Palavra | Similaridade |
|---|---|
| abobado | 0.4658 |
| portão | 0.4316 |
| mexa | 0.4316 |
| expelliarmus | 0.4298 |
| pensativa | 0.4292 |
| observando-a | 0.4235 |
| grunhiu | 0.4178 |
| rony | 0.4177 |
| automaticamente | 0.4174 |
| facilidade | 0.4167 |

**Similaridade entre pares:**
| Par | Alter. 2 | Skip-gram | Variação |
|---|---|---|---|
| harry ↔ rony | 0.3005 | 0.4177 | ↑ +0.1172 |
| harry ↔ hermione | 0.2711 | 0.1646 | ↓ −0.1065 |
| harry ↔ sonserina | −0.0196 | 0.1443 | ↑ +0.1639 |
| harry ↔ grifinória | 0.1325 | 0.1938 | ↑ +0.1613 |

**Aritmética vetorial** (`harry + sonserina − draco`): `reserva` (0.3642)

O Skip-gram mantém similaridades baixas e realistas, o que é positivo. No `most_similar("harry")` aparece `expelliarmus`, o feitiço mais associado a Harry na narrativa, o que é um sinal claro de que o modelo aprendeu associações específicas do universo. No entanto, `hermione` não aparece no top 10, o que é uma limitação. O `most_similar("casa")` não conseguiu capturar as casas de Hogwarts — os resultados são genéricos e pouco informativos. A aritmética vetorial devolveu `reserva`, um resultado sem significado claro, claramente inferior ao `grifinória` do modelo anterior. O Skip-gram produziu embeddings mais específicos em alguns casos, mas a aritmética vetorial foi menos coerente do que na Alteração 2.

---

## Conclusão

| Modelo | Similaridades | most_similar | Aritmética Vetorial |
|---|---|---|---|
| Base (CBOW, 100d, 5ep) | Irrealistas (~0.99) | Verbos genéricos | hermione (razoável) |
| CBOW, 200d, 5ep | Ainda mais altas | Verbos + ruído | mão (sem sentido) |
| CBOW, 200d, w=8, 30ep | Realistas (0.27–0.50) | Personagens relevantes | **grifinória ✓** |
| Skip-gram, 200d, w=8, 30ep | Realistas (0.16–0.42) | Termos específicos do universo | reserva (fraco) |

O modelo CBOW com `window=8` e `epochs=30` produziu os resultados semanticamente mais coerentes, nomeadamente na aritmética vetorial. O aumento de épocas e da janela de contexto revelou-se a alteração mais impactante — muito mais do que aumentar o `vector_size`. O Skip-gram aprendeu associações mais específicas (como `expelliarmus`) mas foi menos eficaz nas analogias, o que pode ser explicado pela dimensão reduzida do corpus, já que o Skip-gram tende a beneficiar mais de corpora maiores.

---

## Exportação do Modelo

```python
model.wv.save_word2vec_format('model_harry.txt', binary=False)
```
```bash
python -m gensim.scripts.word2vec2tensor -i model_harry.txt -o model_harry
```

O modelo final (Skip-gram) é guardado em formato `.txt` compatível com o standard Word2Vec e convertido para os ficheiros `model_harry_tensor.tsv` e `model_harry_metadata.tsv`, necessários para visualização no **TensorFlow Embedding Projector**. O vocabulário final carregado tem **6989 palavras** com vetores de dimensão 200.
