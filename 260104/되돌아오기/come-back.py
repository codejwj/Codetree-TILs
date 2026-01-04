N = int(input())

x, y = 0, 0
dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

ans = 0
found = False

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

    for _ in range(dist):
        x += dxs[move] 
        y += dys[move] 
        ans += 1
        if x == 0 and y == 0:
            found = True
            break
    
    if found:
        break
            
if found:
    print(ans)
else:
    print(-1)