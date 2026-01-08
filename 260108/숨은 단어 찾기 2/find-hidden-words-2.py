N, M = tuple(map(int, input().split()))
arr = [input() for _ in range(N)]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

dxs = [0, 0, 1, -1, 1, 1, -1, -1]
dys = [1, -1, 0 ,0, 1, -1, 1, -1]

cnt = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'L':
            for i in range(8):
                nx2, ny2 = r + dxs[i], c + dys[i]
                nx3, ny3 = r + dxs[i] * 2, c + dys[i] * 2

                if in_range(nx2, ny2) and arr[nx2][ny2] == 'E':
                    if in_range(nx3, ny3) and arr[nx3][ny3] == 'E':
                        cnt += 1 

print(cnt)