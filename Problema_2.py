with open('numere.txt','r') as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    with open('produs.txt','w') as f:
        f.write(str(int(a)*2))
        f.write('\n')
        f.write(str(int(b)*3))
if int(a)<int(b):
    with open('produs.txt','w') as f:
        f.write(str(int(b)*2))
        f.write('\n')
        f.write(str(int(a)*3))
if int(a)==int(b):
    with open('produs.txt','w') as f:
        f.write('Numerele sunt egale')