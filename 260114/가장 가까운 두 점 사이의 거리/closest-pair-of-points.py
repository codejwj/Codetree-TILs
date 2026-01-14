import sys

INT_MAX = sys.maxsize

N = int(input())
points = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

def dist(x, y):
    x1, y1 = points[x]
    x2, y2 = points[y]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

min_dist = INT_MAX
for i in range(N):
    for j in range(i + 1, N):
        min_dist = min(min_dist, dist(i, j))

print(min_dist)