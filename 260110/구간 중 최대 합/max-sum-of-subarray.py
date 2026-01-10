import sys

INT_MIN = -sys.maxsize

N, K = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = INT_MIN
for i in range(N - K + 1):
    sum_val = 0
    for j in range(i, i + K):
        sum_val += arr[j]
    
    ans = max(ans, sum_val)

print(ans)