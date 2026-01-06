N = int(input())
grid = [
    list(map(int, input().split())) 
    for _ in range(N)
]

max_cnt = 0
for i in range(N):
    for j in range(N - 2):
        cnt = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        max_cnt = max(max_cnt, cnt)
        
print(max_cnt)