N = int(input())
x = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

overlapped = [0] * N

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        if (x[i][0] - x[j][0]) * (x[i][1] - x[j][1]) < 0:
            overlapped[i] = 1
            overlapped[j] = 1
            
for elem in overlapped:
    if elem == 0:
        cnt += 1

print(cnt)