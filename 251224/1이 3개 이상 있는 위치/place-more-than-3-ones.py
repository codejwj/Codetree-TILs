N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

ans = 0
for i in range(N):
    for j in range(N):
        x, y = i, j
        cnt = 0
        for dx, dy in zip(dxs, dys):   
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)