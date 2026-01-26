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

    satisfied = False
    for x1, x2 in segments:
        if x1 == segments[i][0] and x2 == segments[i][1]:
            continue

        max_x1 = max(max_x1, x1)
        min_x2 = min(min_x2, x2)

        if max_x1 <= min_x2:
            satisfied = True
            break

if satisfied:
    print("Yes")
else:
    print("No")     