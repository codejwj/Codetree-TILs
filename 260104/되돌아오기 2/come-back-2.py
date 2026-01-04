D = input()

x, y = 0, 0
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

ans = 0
found = False

dir_num = 3
for elem in D:
    if elem == 'L':
        dir_num = (dir_num - 1 + 4) % 4
        ans += 1
    elif elem == 'R':
        dir_num = (dir_num + 1) % 4
        ans += 1
    elif elem == 'F':
        x += dxs[dir_num]
        y += dys[dir_num]
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