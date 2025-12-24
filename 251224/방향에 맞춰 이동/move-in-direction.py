N = int(input())

x, y = 0, 0
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

for _ in range(N):
    D, dist = tuple(input().split())
    dist = int(dist)

    if D == 'E':
        move = 0
    elif D == 'W':
        move = 1
    elif D == 'S':
        move = 2
    else:
        move = 3
    
    x += dx[move] * dist
    y += dy[move] * dist

print(x, y)