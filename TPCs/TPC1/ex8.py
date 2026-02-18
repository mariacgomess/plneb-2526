def ocr(s1,s2):
    ls1=len(s1)
    c=0
    i=0
    while i<(len(s2)-len(s1)):

        if s2[i:(i+ls1)]==s1:      
            c=c+1
            i=i+ls1
        else:
            i=i+1
    print(c)

ocr("na","bananas")