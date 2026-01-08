N, M = tuple(map(int, input().split()))
arr = [
    input() 
    for _ in range(N)
]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

#가로, 세로, 대각선으로 인접한 8칸
dxs = [0, 0, 1, -1, 1, 1, -1, -1]
dys = [1, -1, 0 ,0, 1, -1, 1, -1]

cnt = 0
#모든 좌표에서 다 확인
for r in range(N):
    for c in range(M):
        #시작점 'L' 찾기
        if arr[r][c] != 'L':
            continue

        for dx, dy in zip(dxs, dys):
            nx1, ny1 = r + dx, c + dy
            nx2, ny2 = r + dx * 2, c + dy * 2

            if in_range(nx1, ny1) and arr[nx1][ny1] == 'E':
                if in_range(nx2, ny2) and arr[nx2][ny2] == 'E':
                    cnt += 1 

print(cnt)