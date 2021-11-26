with open('Caractere.txt','r')as f:
    a=f.read()
with open('Vocale.txt','w')as f:
    for i in range(len(a)):
        if a[i] in ('a','e','u','i','o','â','ă','î','A','E','U','I','O','Ă','Î','Â'):
            f.write(a[i])