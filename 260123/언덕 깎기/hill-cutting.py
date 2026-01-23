import sys

INT_MAX = sys.maxsize

N = int(input())
H = [
    int(input()) 
    for _ in range(N)
]

ans = INT_MAX
for h in range(100 - 17 + 1):
    cost = 0
    for i in range(N):
        if H[i] < h:
            cost += (h - H[i])  ** 2
        elif H[i] > h + 17:
            cost += (H[i] - (h + 17)) ** 2

    ans = min(ans, cost)

print(ans)