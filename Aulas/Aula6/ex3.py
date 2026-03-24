import spacy
from spacy.matcher import Matcher

nlp=spacy.load("pt_core_news_sm")
f = open(r"C:\Users\Maria\Desktop\Universidade\mestrado\PLN\plneb-2526-prof\Dados\Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf-8")
texto = f.read()
doc = nlp(texto)

matcher = Matcher(nlp.vocab)

pattern = [{"ENT_TYPE": "PER", "OP": "+"},  # entidade do tipo pessoa
           {"POS": {"IN": ["VERB", "AUX"]}, "OP": "+"},  #1 ou mais verbos
           {"POS": "DET", "OP": "?"},
           {"POS": "NOUN"}]

matcher.add("match_id", [pattern])
matches = matcher(doc)

for id, start, end in matches:
    print(doc[start:end])

print(len(matches))