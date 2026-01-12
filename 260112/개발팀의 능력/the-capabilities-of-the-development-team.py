import sys

INT_MAX = sys.maxsize

N = 5
arr = list(map(int, input().split()))

def diff(x, y, z):
    if arr[x] == arr[y] == arr[z]:
        return -1
        
    sum1 = arr[x] + arr[y]
    sum2 = arr[z]
    sum3 = sum(arr) - sum1 - sum2
    return abs(max(sum1, sum2, sum3) - min(sum1, sum2, sum3))

min_diff = INT_MAX
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            min_diff = min(min_diff, diff(i, j, k))

print(min_diff)