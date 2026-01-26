import sys

INT_MAX = sys.maxsize

N = int(input())
segments = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

for i in range(N):
    max_x1 = 0
    min_x2 = INT_MAX
    for j in range(N):
        if j == i:
            continue
        
        max_x1 = max(max_x1, segments[j][0])
        min_x2 = min(min_x2, segments[j][1])

    if max_x1 <= min_x2:
        print("Yes")
        sys.exit()

print("No")     