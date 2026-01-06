R, C = map(int, input().split())
grid = [
    list(input().split()) 
    for _ in range(R)
]

cnt = 0
for r1 in range(1, R - 2):
    for c1 in range(1, C - 2):
        if grid[r1][c1] != grid[0][0]:
            for r2 in range(r1 + 1, R - 1):
                for c2 in range(c1 + 1, C - 1):
                    if grid[r2][c2] != grid[r1][c1]:
                        if grid[r2][c2] != grid[R - 1][C - 1]:
                            cnt += 1

print(cnt)