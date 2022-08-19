n = int(input())

for i in range(n) :
    score = list(map(int, input().split()))
    av = sum(score[1:])/score[0]
    cnt = 0
    for i in score[1:] :
        if i > av :
            cnt += 1
    p = cnt/score[0] *100
    print(f"{p:.3f}%")