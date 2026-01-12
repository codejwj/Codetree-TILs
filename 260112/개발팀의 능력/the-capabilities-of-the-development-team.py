import sys

INT_MAX = sys.maxsize

N = 5
arr = list(map(int, input().split()))

def diff(x, y, z):
    sum1 = arr[x]
    sum2 = arr[y] + arr[z]
    sum3 = sum(arr) - sum1 - sum2

    if sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
        return INT_MAX

    return abs(max(sum1, sum2, sum3) - min(sum1, sum2, sum3))

min_diff = INT_MAX
for i in range(N):
    for j in range(N):
        for k in range(j + 1, N):
            if i == k or i == j:
                continue

            min_diff = min(min_diff, diff(i, j, k))

if min_diff == INT_MAX:
    print(-1)
else:
    print(min_diff)