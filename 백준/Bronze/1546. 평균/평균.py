n = int(input())
score = list(map(int, input().split()))
m = max(score)

new_list = []
for i in score :
    new_list.append(i/m*100)

print(sum(new_list)/n)