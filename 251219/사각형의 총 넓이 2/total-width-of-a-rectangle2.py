OFFSET = 100

N = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

plane = [[0] * 200 for _ in range(200)]

for k in range(N):
    for i in range(x1[k] + OFFSET, x2[k] + OFFSET):
        for j in range(y1[k] + OFFSET, y2[k] + OFFSET):
            plane[i][j] = 1

total = 0
for row in plane:
    total += sum(row)

print(total)