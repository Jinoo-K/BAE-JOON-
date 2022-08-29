dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

text = input()
sum = 0

for i in text:
    for j in dial: 
        if i in j:
            sum += dial.index(j)+3

print(sum)