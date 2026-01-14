import sys

INT_MAX = sys.maxsize

N = int(input())
arr = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

min_size = INT_MAX
for i in range(N):
    x1, x2 = INT_MAX, 1
    y1, y2 = INT_MAX, 1
    for j, (x, y) in enumerate(arr):
        #i번째 점은 제외
        if j == i:
            continue
        
        x1 = min(x1, x)
        y1 = min(y1, y)
        x2 = max(x2, x)
        y2 = max(y2, y)

    size = (x2 - x1) * (y2 - y1)
    min_size = min(min_size, size)

print(min_size)