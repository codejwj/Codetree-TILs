import sys

INT_MAX = sys.maxsize

N, H, T = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = INT_MAX
for i in range(N - T + 1):
    cost = 0
    for j in range(i, i + T):
        cost += abs(arr[j] - H)
    
    ans = min(ans, cost)

print(ans)