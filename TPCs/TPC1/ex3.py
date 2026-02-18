def vowels(s):
    n=0
    ns=s.lower()
    for l in ns:
        if l in ["a","e","i","o","u"]:
            n=n+1
    print(n)

vowels("A Maria toca guitarra")