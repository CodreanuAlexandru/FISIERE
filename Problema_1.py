with open('numere.txt','r') as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    with open('minim.txt','w') as f:
        f.write(b)
if int(a)<int(b):
    with open('minim.txt','w') as f:
        f.write(a)
if int(a)==int(b):
    with open('minim.txt','w') as f:
        f.write('Numerele sunt egale')