import spacy
import math

nlp=spacy.load("en_core_news_sm")
collection=["The sky is blue",
            "The sun is bright",
            "The sun in the sky"]

#remover stopwords, pontuação e por tudo em minuscula, tokenizar
def pre_processamento(collection):
    new_collection=[]
    for doc in collection:
        s_doc=nlp(doc)
        ...
        """new_collection=[
            ["sky","blue"],
            ["sun","bright"],
            ["sun","sky"]
        ]"""
    return new_collection

def tf(d):#frequencia em cada documento
    N=len(d)
    res={}
    for term in d:
        if term in res:
            res[term]+=1
        else:
            res[term]=1
    
    res={k:v/N for k, v in res.items}
    return res
    

def idf(collection):#raridade em todos os documentos
    res={}
    N=len(collection)
    unique_terms=set([term for d in collection for term in d])
    for term in unique_terms:
        counter=0
        for doc in collection:
            if term in doc:
                counter+=1
        rarity=math.log(N/counter,10)
        res[term]=rarity

    return res

def tf_idf(collection):
    res=[]
    idf_values=idf(collection)
    for doc in collection:
        doc_tf_idf=[]
        tf_values=tf(doc)
        tf_values=tf(doc)
        for term in tf_values:
            tf_idf=tf_values[term]*idf_values[term]
            doc_tf_idf.append(tf_idf)
        res.append(doc_tf_idf)
    return res

tf_idf(collection)
    
   
#query "the bright sun", calcular tf da query e usar o idf do corpus (multiplicar tf idf) fazer o vetor e calcular o cosseno entre o vetor da query e o vetor de ns que para ver o doc mais relevante