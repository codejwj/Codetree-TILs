import sys

INT_MIN = -sys.maxsize

N, K = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

max_sum = INT_MIN
for i in range(N - K + 1):
    sum_val = 0
    for j in range(i, i + K):
        sum_val += arr[j]
    
    max_sum = max(max_sum, sum_val)

print(max_sum)