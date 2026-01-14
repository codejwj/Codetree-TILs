import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

min_size = INT_MAX
for i in range(N):
    x1, x2 = INT_MAX, INT_MIN
    y1, y2 = INT_MAX, INT_MIN
    for j in range(N):
        if j == i:
            continue
        
        x, y = arr[j]
        x1 = min(x1, arr[j][0])
        y1 = min(y1, arr[j][1])
        x2 = max(x2, arr[j][0])
        y2 = max(y2, arr[j][1])

    size = (x2 - x1) * (y2 - y1)
    min_size = min(min_size, size)

print(min_size)