D = input()

x, y = 0, 0
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

dir_num = 3
for elem in D:
    if elem == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif elem == 'R':
        dir_num = (dir_num + 1) % 4   
    elif elem == 'F':
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)