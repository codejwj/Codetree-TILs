N = int(input())
moves = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

cnt1 = 0
cnt2 = 0
for i in range(N):
    if 1 < 2 or 2 < 3 or 3 < 1:
        if moves[i][0] > moves[i][1]:
            cnt1 += 1
        elif moves[i][0] < moves[i][1]:
            cnt2 += 1
        else:
            pass

print(max(cnt1, cnt2))