OFFSET = 100
MAX_R = 200

N = int(input())
rects = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for x1, y1 in rects:
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    for x in range(x1, x1 + 8):
        for y in range(y1, y1 + 8):
            checked[x][y] = 1

area = 0
for x in range(0, MAX_R + 1):
    for y in range(0, MAX_R + 1):
        if checked[x][y]:
            area += 1

print(area)