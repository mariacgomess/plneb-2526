import spacy
nlp = spacy.load("./models/model-best")
f=open(r"C:\Users\Maria\Desktop\Universidade\mestrado\PLN\plneb-2526-prof\Dados\Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf-8")
texto=f.read()
ruler=nlp.add_pipe("entity_ruler", last=True)
config = {
    "overwrite_ents": True,
}
patterns=[
    {"label": "Pessoa","pattern":"Dumbledore"},
    {"label": "Pessoa","pattern":"Dumbledore"},
    {
        "label": "Pessoa",
        "pattern":[{"LOWER":"albus"},{"LOWER":"dumbledore"}]
    }
]
ruler.add_patterns(patterns)

doc=nlp(texto)
for ent in doc.ents:
    print(ent, ent.label_)

