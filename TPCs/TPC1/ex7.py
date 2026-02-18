def balanc(s1,s2):
    b=True
    for l in s1:
        if l not in s2:
            b=False
    print(b)

balanc("erro","torre")
balanc("torre","erro")


