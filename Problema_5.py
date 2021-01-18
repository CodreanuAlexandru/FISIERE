with open('numar.txt','r') as f:
    a=f.read()
with open('inmultire.txt','w') as f:
    for x in range(1,11):
        f.write(str(x))
        f.write('*')
        f.write(a)
        f.write('=')
        f.write(str(int(a)*x))
        f.write('\n')