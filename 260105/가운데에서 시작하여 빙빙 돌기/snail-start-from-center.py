N = int(input())
arr = [[0] * N for _ in range(N)]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

x, y = N // 2, N // 2
dir_num = 3

arr[x][y] = 1

for i in range(2, N * N + 1):
    nx = x + dxs[(dir_num + 1) % 4]
    ny = y + dys[(dir_num + 1) % 4]
    if in_range(nx, ny) and arr[nx][ny] == 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for i in range(N):
    for j in range(N):
        print(arr[i][j], end = ' ')
    print()