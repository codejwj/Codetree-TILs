OFFSET = 100

N = int(input())
rects = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

checked = [[0] * 201 for _ in range(201)]

for x1, y1, x2, y2 in rects:
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j] = 1

area = 0
for x in range(0, 201):
    for y in range(0, 201):
        if checked[x][y]:
            area += 1

print(area)