total = int(input())
n = int(input())
sum = 0

for n in range(1, n+1) :
    price, ea = map(int, input().split())
    won = price * ea
    sum += won
    
if sum == total :
    print("Yes")
else :
    print("No")