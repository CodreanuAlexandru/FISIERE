with open('/home/alex/Documents/.vscode/Lista clasei 11C.txt','r') as f:
    a=f.readlines()
n,m=0,0
with open('Lista Engleza','w')as f:
    for z in a:
        c=z.split()
        nota=int(c[2])
        n,m=n+1,m+nota
        print(c[0],c[1],nota)
        if 'Engleza'in c[3]:
            f.write(str(z))
with open('Lista Franceza','w')as f:
    for v in a:
        b=v.split()
        if 'Franceza'in b[3]:
            f.write(str(v))
print('Media celor',n,'elevi este',m/n)