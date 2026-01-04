N, T = tuple(map(int, input().split()))
D = input()
grid = [
    list(map(int, input().split())) 
    for _ in range(N)
]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N
    
x, y = N // 2, N // 2
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

dir_num = 3
ans = grid[x][y]

for elem in D:
    if elem == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif elem == 'R':
        dir_num = (dir_num + 1) % 4
    elif elem == 'F':
        nx = x + dxs[dir_num]
        ny = y + dys[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny
            ans += grid[x][y]
            
print(ans)