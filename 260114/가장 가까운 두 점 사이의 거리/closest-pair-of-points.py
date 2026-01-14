import sys

INT_MAX = sys.maxsize

N = int(input())
points = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

min_dist = INT_MAX
for i in range(N):
    for j in range(i + 1, N):
        dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        min_dist = min(min_dist, dist)

print(min_dist)