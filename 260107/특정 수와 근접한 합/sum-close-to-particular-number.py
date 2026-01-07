import sys

INT_MAX = sys.maxsize

N, S = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

total_sum = sum(arr)
ans = INT_MAX

for i in range(N):
    for j in range(i + 1, N):
        sum_val = total_sum - (arr[i] + arr[j])
        diff = abs(S - sum_val)
    
        ans = min(ans, diff)

print(ans)