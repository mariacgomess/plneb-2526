def anagrama(s1,s2):
    b=True
    for l in s1:
        if l not in s2:
            b=False
    for l in s2:
        if l not in s1:
            b=False
    print(b)

anagrama("listen","silent")
anagrama("hello","world")