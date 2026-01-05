N, M = tuple(map(int, input().split()))
arr = [
    [0] *N
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
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    
    return cnt

for _ in range(M):
    r, c = tuple(map(int, input().split()))
    arr[r - 1][c - 1] = 1

    if adjacent_cnt(r - 1, c - 1) == 3:
        print(1)
    else:
        print(0)