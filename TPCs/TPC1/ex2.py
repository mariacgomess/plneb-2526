def counta(s):
    n=0
    for l in s:
        if l in ["A","a"]:
            n=n+1
    print(n)

counta("A Maria toca guitarra")