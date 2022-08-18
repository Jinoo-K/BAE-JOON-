n = int(input())
star = 1

for i in range(n):
    print(str("*"*star).rjust(n))
    star += 1