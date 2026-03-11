import re
import json
f =open('dicionario_medico.xml','r',encoding='utf8')
text=f.read()

text=re.sub(r"</?text.*?>","",text)
text=re.sub(r"</?page.*?>","",text)
#text=re.sub(r"</b>","",text)

f2=open("dicionario_medico_tratado.xml", "w", encoding="utf-8")
f2.write(text)

#conceitos=re.split(r"<b>",text)
conceitos=re.findall(r"<b>(.*)</b>\n([^<]+)\s*",text)
res={}
for termo, desc in conceitos:
    res[termo]=desc.strip()

f_out = open("conceitos.json","w", encoding="utf8")
json.dump(res, f_out, indent=4, ensure_ascii=False)
f_out.close()
print(len(conceitos))