import re
text="Olá tudo bem Tom ? Tudo perfeito neste ano de 2026! aMuito Muito Mesmo muito 3,14"
print(re.search(r'tudo',text))
print(re.findall(r'[tT]udo',text))
print(re.findall(r'\w',text))
print(re.findall(r'\d',text))
print(re.findall(r'\d+,\d+',text))
print(re.findall(r'\w{3,}',text))
print(re.findall(r'\b[^m]*M[^m]*\b',text))

