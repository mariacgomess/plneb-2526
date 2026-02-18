def reverse2(s):
    ns=""
    for l in s[::-1]:
        ns=ns+l
    return ns 

def capicua(s):
    ns=s.lower()
    capicua=False
    if ns==reverse2(ns):
        capicua=True
    print (capicua)

capicua("Ana")
capicua("Maria")
capicua("20:02")