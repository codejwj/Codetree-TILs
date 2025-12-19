OFFSET = 1000
MAX_R = 2000

N = 2
rects = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for i, (x1, y1, x2, y2) in enumerate(rects, start = 1):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] = i

area = 0
min_x, max_x = MAX_R, 0
min_y, max_y = MAX_R, 0
exist = False

for x in range(0, MAX_R + 1):
    for y in range(0, MAX_R + 1):
        if checked[x][y] == 1:
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)
            exist = True

if not exist:
    print(0)
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

print(area)