def reverse1(s):
    slist=s.split(" ")
    ns=""
    for w in reversed(slist):
        ns=ns+w
        ns=ns+" "
    print(ns)

def reverse2(s):
    ns=""
    for l in s[::-1]:
        ns=ns+l
    print(ns) 

reverse1("A Maria toca guitarra")
reverse2("A Maria toca guitarra")