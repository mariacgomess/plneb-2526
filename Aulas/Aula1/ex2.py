y=input("Insere a tua lista de números com , entre cada número")
lista=y.split(",")
nova=[]
for n in lista:
    n=int(n)
    
    if n%2==0:
        nova.append(n)
print(nova)