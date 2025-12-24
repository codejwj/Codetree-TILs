N = int(input())

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for _ in range(N):
    D, d = tuple(input().split())
    d = int(d)

    if D == 'E':
        move = 0
    elif D == 'S':
        move = 1
    elif D == 'W':
        move = 2
    else:
        move = 3
    
    x, y = x + d * dx[move], y + d * dy[move]

print(x, y)