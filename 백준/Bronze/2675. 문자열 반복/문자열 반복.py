n = int(input())

for i in range(n):
    cnt, word = input().split()
    cnt = int(cnt)
    for i in word :
        print (int(cnt)*i, end="")
    print()