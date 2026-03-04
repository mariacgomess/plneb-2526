# Tratamento de Dicionário Médico (PDF → TXT)

## Objetivo

Este trabalho tem como objetivo **remover quebras de página e reconstruir corretamente o texto**
de um dicionário médico convertido de **PDF para TXT**.

A conversão PDF para TXT introduz vários problemas, levando a que o texto neste novo formato apareça desformatado. Neste exercício tratamos as quebras de página (`\f`) que estavam a separar incorretamento os conceitos das suas definições e também a partir estas definições ao meio. Neste exercício começamos por ler o ficheiro de texto "dicionario_medico.txt", que for previamente passado de formato PDF para este, depois tratamos as anomalias de formatação com recurso a expressões regulares, e finalmente adaptamos o documento modificado para listas, dicionários e formato html.

## 1 - Leitura do ficheiro

O ficheiro original é lido em formato UTF-8 para preservar caracteres acentuados. Utilizamos o código abaixo para a leitura do ficheiro.

f=open('dicionario_medico.txt','r',encoding='utf8')
text=f.read()

Para ir verificando o estado do ficheiro após o tratamento, criamos um novo ficheiro de texto para escrever o texto tratado, para tal utilizamos o código abaixo.


f2=open("dicionario_medico_tratado.txt", "w", encoding="utf-8")
f2.write(text)

## 2 - Tratamento da formatação

Começamos por marcar os conceitos e respetivas definições, que são antecedidas por \n\n, substituindo isto por \n\n@. Normalmente isto apenas isolaria os conceitos e suas definições uns dos outros mas devido as quebras de página também pode serpar definições de conceitos,ou partir as definições, algo que iremos resolver mais a frente. 

De seguida removemos as quebras de página que apareciam nos documentos como um sinal vermelho com ff, substituindo \f por \n.


De seguida resolvemos o problema das quebras, e para tal utilizamos o seguinte código:

para resolver quebras entre conceitos e definições: text=re.sub(r'\n\n@\n([A-ZÀ-Ú])',r'\n\1',text)

Como as definições começam sempre por maiúscula e os conceitos por minúscula, isto vai permitir nos identificar um @ antes de uma definição, que estará a identificar a separação desta do respetivo conceito. Usamos os () e o \1 para manter a letra que é o fator chave para perceber que aquilo é uma definição.

para resolver quebras no meio de definições:text = re.sub(r'([a-zà-ú])\s*\n\n@\n\s*([a-zà-ú])',r'\1 \2',text)

Neste caso iriamos ter os parágrafos e o @ entre duas letras minúsculas, que podem ou não ter um espaço antes ou depois, no caso da ultima letra antes e na primeira letra depois da quebra respetivamente. Mais uma vez utilizamos () e o \1 e \2 para manter as duas letras que usamos para identificar a quebra no meio da definição, colocando um espaço entre eles para o caso deste ser apagado na substituição.Isto não vai interferir com quebras entre o final de uma definição e o conceito seguinte, pois as definições acabam sempre com pontuação.

Finalmente, removemos os @ deixando apenas os parágrafos (\n) a separar os conceitos e respetivas definições uns dos outros.

Ainda rescrevemos o ficheiro todo com as novas alterações, como referido anteriormente, para durante o processo de tratamento perceber melhor a estrutura que o ficheiro ia tomando e como resolver os problemas de formatação.

## 3- Listas, dicionários html

Como tinhamos feito nas aulas, ainda utilizamos o re.split para criar uma lista com os conceitos e respetivas definições, dividindo pelo \n, criamos um dicionário com key=conceito e value=definição, e ainda um html com a informação do ficheiro de texto tratado.