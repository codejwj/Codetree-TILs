N = int(input())
grid = [
    list(map(int, input().split())) 
    for _ in range(N)
]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

def adjacent_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1
    
    return cnt

ans = 0
for i in range(N):
    for j in range(N):
        if adjacent_cnt(i, j) >= 3:
            ans += 1

print(ans)