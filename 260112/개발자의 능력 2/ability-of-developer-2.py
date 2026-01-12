import sys

INT_MAX = sys.maxsize

arr = list(map(int, input().split()))

def diff(w, x, y, z):
    sum1 = arr[w] + arr[x]
    sum2 = arr[y] + arr[z]
    sum3 = sum(arr) - sum1 - sum2
    return abs(max(sum1, sum2, sum3) - min(sum1, sum2, sum3))

min_diff = INT_MAX
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(4):
            for l in range(k + 1, 4):
                min_diff = min(min_diff, diff(i, j, k, l))

print(min_diff)