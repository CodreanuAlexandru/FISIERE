with open('input.txt','r') as f:
    a=f.read()
print(type(a))
with open('output.txt','w') as f:
    f.write(str(int(a)-2))
    f.write(' ')
    f.write(str(int(a)-1))
    f.write(' ')
    f.write(str(int(a)))
    f.write(' ')
    f.write(str(int(a)+1))
    f.write(' ')
    f.write(str(int(a)+2))