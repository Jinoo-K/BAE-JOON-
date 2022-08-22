num_list = list(map(int, input().split()))
a = num_list[0]
b = num_list[1]
a = int(str(a)[::-1])
b = int(str(b)[::-1])

if a > b :
    print(a)
else :
    print(b)
