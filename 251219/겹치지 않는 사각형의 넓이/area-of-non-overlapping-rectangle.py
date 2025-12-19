OFFSET = 1000
MAX_R = 2000

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
M = tuple(map(int, input().split()))

checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for rect in [A, B]:
    x1, y1, x2, y2 = rect
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j] = 1

x1, y1, x2, y2 = M
x1, y1 = x1 + OFFSET, y1 + OFFSET
x2, y2 = x2 + OFFSET, y2 + OFFSET
for i in range(x1, x2):
    for j in range(y1, y2):
        checked[i][j] = 0

area = 0
for x in range(0, MAX_R + 1):
    for y in range(0, MAX_R + 1):
        if checked[x][y]:
            area += 1

print(area)