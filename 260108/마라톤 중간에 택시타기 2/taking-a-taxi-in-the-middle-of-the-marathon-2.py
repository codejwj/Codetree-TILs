import sys

INT_MAX = sys.maxsize

N = int(input())
P = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

min_dist = INT_MAX

for i in range(1, N - 1):
    dist = 0
    prev_idx = 0
    for j in range(1, N):
        if j == i:
            continue

        dx = abs(P[j][0] - P[prev_idx][0])
        dy = abs(P[j][1] - P[prev_idx][1]) 
        dist += dx + dy

        prev_idx = j
    
    min_dist = min(min_dist, dist)

print(min_dist)