t = int(input())
s = 1

for i in range(t) :
    a, b = map(int, input().split())
    print(f"Case #{s}:", a+b)
    s += 1