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
        remains = [idx for idx in range(6) if idx != i and idx != j]
        for k in range(len(remains)):
            for l in range(k + 1, len(remains)):
                min_diff = min(min_diff, diff(i, j, remains[k], remains[l]))

print(min_diff)