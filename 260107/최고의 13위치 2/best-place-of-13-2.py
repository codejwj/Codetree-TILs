N = int(input())
arr = [
    list(map(int, input().split())) 
    for _ in range(N)
]

max_cnt = 0
for i in range(N):
    for j in range(N - 2):
        for k in range(i + 1, N):
            for l in range(N - 2):
                cnt = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                
                max_cnt = max(max_cnt, cnt)

print(max_cnt)