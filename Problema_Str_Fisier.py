with open('Text.txt', 'r') as f:
    sir=list(f.read())
with open('LitereA.txt', 'w') as f:
    f.write(str(list(filter(str.isupper, sir))))
with open('LitereB.txt', 'w') as f:
    f.write(str(list(filter(str.islower, sir))))
with open('Semnedepuntuatie.txt', 'w') as f:
    f.write(str(list(filter(lambda a: a in ['[',']','(',')','{','}',"'",'*','/','//','%','**',',',';','.','!'],sir))))
with open('Cifrele.txt', 'w') as f:
    f.write(str(list(filter(lambda b: b in ['1','2','3','4','5','6','7','8','9'], sir))))