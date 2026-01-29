N = int(input())
moves = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

cnt1 = 0
cnt2 = 0
for i in range(N):
    if moves[i][0] == 1:
        if moves[i][1] == 3:
            cnt1 += 1
        elif moves[i][1] == 2:
            cnt2 += 1
    elif moves[i][0] == 2:
        if moves[i][1] == 1:
            cnt1 += 1
        elif moves[i][1] == 3:
            cnt2 += 1
    elif moves[i][0] == 3:
        if moves[i][1] == 2:
            cnt1 += 1
        elif moves[i][1] == 1:
            cnt2 += 1
        
print(max(cnt1, cnt2))