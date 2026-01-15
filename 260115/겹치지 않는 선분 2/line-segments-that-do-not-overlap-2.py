N = int(input())
x = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

cnt = 0
for i in range(N):
    overlap = False
    for j in range(N):
        if j == i:
            continue
            
        if (x[i][0] - x[j][0]) * (x[i][1] - x[j][1]) < 0:
            overlap = True
            break
    
    if overlap == False:
        cnt += 1

print(cnt)