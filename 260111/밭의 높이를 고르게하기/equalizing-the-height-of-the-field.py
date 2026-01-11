import sys

INT_MAX = sys.maxsize

N, H, T = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

min_cost = INT_MAX
for i in range(N - T + 1):
    cost = 0
    for j in range(i, i + T):
        cost += abs(arr[j] - H)
    
    min_cost = min(min_cost, cost)

print(min_cost)