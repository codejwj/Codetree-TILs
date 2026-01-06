N = int(input())
grid = [
    list(input()) 
    for _ in range(N)]

K = int(input())

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

if 1 <= K <= N:
    x, y = 0, K - 1
    dir_num = 0
elif N + 1 <= K <= 2 * N:
    x, y = K - N - 1, N - 1
    dir_num = 1
elif 2 * N + 1 <= K <= 3 * N:
    x, y = N - 1, 3 * N - K
    dir_num = 2
elif 3 * N + 1 <= K <= 4 *N:
    x, y = 4 * N - K, 0
    dir_num = 3

ans = 0
while in_range(x, y):
    if grid[x][y] == '/':
        dir_num = dir_num ^ 1
    elif grid[x][y] == '\\':
        dir_num = 3 - dir_num
    
    ans += 1
    x += dxs[dir_num]
    y += dys[dir_num]

print(ans)