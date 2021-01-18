with open('globulet.txt','r') as f:
    a=f.read()
with open('bradut.txt','w') as f:
    f.write(str(int(a)*6))