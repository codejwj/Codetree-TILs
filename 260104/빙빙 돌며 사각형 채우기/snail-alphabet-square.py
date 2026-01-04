N, M = map(int, input().split())
arr = [
    [0] * M
    for _ in range(N)
]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y = 0, 0
dir_num = 0

arr[x][y] = 1

for i in range(2, N * M + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for i in range(N):
    for j in range(M):
        print(chr(((arr[i][j] - 1) % 26) + 65), end = ' ')
    print()