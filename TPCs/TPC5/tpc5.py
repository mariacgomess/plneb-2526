from bs4 import BeautifulSoup
import requests
import json
import string
import unicodedata

url = f"https://www.atlasdasaude.pt/doencasAaZ/"

abcedario = string.ascii_lowercase
res = {}
def limpar_doenca(palavra):
    palavra=palavra.lower()
    palavra=palavra.replace(" ", "-")
    palavra = unicodedata.normalize("NFD", palavra)
    palavra = palavra.encode("ascii", "ignore").decode("utf-8")
    return palavra

def extrair_pagina(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    div_doencas = soup.find_all("div", class_="views-row")

    res = {}
    for div in div_doencas:
        designacao = div.div.h3.a.text #no div entra no primeiro div que entra no h3 que entra no a e vai buscar so o texto
        sdescricao = div.find("div", class_="views-field views-field-body").div.text #o .text vai devolver o texto de todos os filhos a partir do ponto que estamos, por isso convem ser o mais especifico possivel
        
        doenca=limpar_doenca(designacao)
        newurl = f"https://www.atlasdasaude.pt/content/{doenca}"
        html2 = requests.get(newurl).text
        fdsoup = BeautifulSoup(html2, "html.parser")

        body_div =fdsoup.find("div",class_="field-name-body")
        if body_div:
            content_div = body_div.find("div", class_="field-item even")
        else:
            content_div = None

        fdescricao=""
        if content_div:
            for elem in content_div.children:

                    if elem.name == "h2":
                        break

                    if elem.name is not None:
                        texto=elem.get_text(strip=True)
                        if texto:
                            fdescricao += texto + " "

                    else:
                         texto_solto=str(elem).strip()
                         if texto_solto:
                            print("c")
                            fdescricao += texto_solto + " "

        descricao={}
        descricao["short"]=sdescricao
        
        descricao["full"]=fdescricao
        res[designacao] = descricao
    return res

for letra in abcedario:
    res = res | extrair_pagina(url+letra) #juntar dicionario

f_out = open("doencas.json", "w", encoding="utf8")
json.dump(res, f_out, indent=4, ensure_ascii=False)
f_out.close()


  