import sys

INT_MAX = sys.maxsize

N = int(input())
points = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

min_dist = INT_MAX
for i in range(N):
    x1, x2 = INT_MAX, 1
    y1, y2 = INT_MAX, 1
    for j, (x, y) in enumerate(points):
        if j == i:
            continue
        
        x1 = min(x1, x)
        y1 = min(y1, y)
        x2 = max(x2, x)
        y2 = max(y2, y)
    
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    min_dist = min(min_dist, dist)

print(min_dist)