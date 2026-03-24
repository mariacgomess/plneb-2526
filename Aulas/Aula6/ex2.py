import spacy

nlp = spacy.load("pt_core_news_sm")

f = open(r"C:\Users\Maria\Desktop\Universidade\mestrado\PLN\plneb-2526-prof\Dados\Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf-8")
texto=f.read()
doc = nlp(texto)

print("="*20, "Tokens", "="*20)
verbos={}
for token in doc:
    
    if token.pos_=="VERB":
        if token.lemma_ in verbos:
            verbos[token.lemma_]+=1
        else:
            verbos[token.lemma_]=1

sorted_verbs=sorted(verbos.items(), key=lambda x:x[1])
print(sorted_verbs)