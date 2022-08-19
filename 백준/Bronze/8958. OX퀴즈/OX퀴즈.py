n = int(input())

for i in range(n) :
    o = input()
    l = list(o)
    sum = 0
    c = 1
    for i in l :
        if i == "O":
            sum += c
            c += 1
        else :
            c = 1
    print(sum)