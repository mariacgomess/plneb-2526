import re
#ler ficheiro txt
f=open('dicionario_medico.txt','r',encoding='utf8')#encoding='utf8'
text=f.read()

#isolar conceitos
text=re.sub(r'\n\n','\n\n@',text)
#quebras de página
text=re.sub(r'\f','\n',text)
#quebras entre def e conc -> é um @\n com uma letra maiuscula a seguir, pois todos os conceitos começam com letra maiuscula
text=re.sub(r'\n\n@\n([A-ZÀ-Ú])',r'\n\1',text) #usamos os () e o \1 para manter a letra
#quebras entre conceitos -> é quando há paragrafos e @ entre duas minusculas que podem ou não ter espaço
#não conta de def para conc pq estes acabam sempre com pontuação
text = re.sub(r'([a-zà-ú])\s*\n\n@\n\s*([a-zà-ú])',r'\1 \2',text)
#desisolar conceitos
text=re.sub(r'@','',text)
print(text)

f2=open("dicionario_medico_tratado.txt", "w", encoding="utf-8")
f2.write(text)





#capturar conceitos e definições
conceitos= re.split(r'\n\n',text,maxsplit=0,flags=0)
print(len(conceitos))

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


print(len(conceitos_dict))

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