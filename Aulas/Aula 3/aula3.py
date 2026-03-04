import re
#ler ficheiro txt
f=open('dicionario_medico.txt','r',encoding='utf8')#encoding='utf8'
text=f.read()

#limpar texto
text=re.sub(r'\f','',text)

#marcar informação
text=re.sub(r'\n\n','\n\n@',text)

#capturar conceitos
#conceitos=re.findall(r'@[^\n]+',text)
#print(conceitos)

#capturar conceitos e definições
conceitos= re.split(r'\n\n@',text,maxsplit=0,flags=0)
print(conceitos)

#conceitos_def2 = re.findall(r'@[^@]+',text,maxsplit=0,flags=0)
#print(conceitos_def2)

#conceitos_def3 = re.split(r'@',text,maxsplit=0,flags=0)
#print(conceitos_def3)
def limpa_descricao(descricao):
    descricao=re.sub(r'\n',' ',descricao)
    descricao= descricao.strip
    return descricao
conceitos_dict={}

for c in conceitos[1:]:
    elems = re.split(r"\n",c)
    if len(elems)>1:
        designacao = elems[0]
        #print("designacao:", designacao)
        descricao = elems[1]
        #print("descricao:", descricao)
        #print("-"*20)
        conceitos_dict[designacao]=descricao
    else:
        continue


print(conceitos_dict)

import json

#json.load() - ler um ficheiro
#json.dump() - criar ficheiro

#f_out = open("dicionario_medico.json", "w")
#json.dump(conceitos_dict, f_out, indent= 4, ensure_ascii=False)

def gera_html(filename, conceitos_dict):
    html="""
<html>
    <head>
    <title> Dicionário Médico </title>
    <head>
    <body>"""
    html_body=""
    for c in conceitos_dict:
        html=html + f"""
        <div>
            <p> {c} </p>
            <p> {conceitos_dict[c]} </p>
        </div>
        """
    html_footer=""    
    """</body>
</html> """
    f_out=open(filename,"w")
    f_out.write(html)

gera_html("dicionario_medico.html", conceitos_dict)