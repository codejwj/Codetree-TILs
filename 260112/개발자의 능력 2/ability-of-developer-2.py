import sys

INT_MAX = sys.maxsize

N = 6
arr = list(map(int, input().split()))

def diff(w, x, y, z):
    sum1 = arr[w] + arr[x]
    sum2 = arr[y] + arr[z]
    sum3 = sum(arr) - sum1 - sum2
    return abs(max(sum1, sum2, sum3) - min(sum1, sum2, sum3))

min_diff = INT_MAX
#첫 번째 팀원
for i in range(N):
    for j in range(i + 1, N):
        #두 번째 팀원
        for k in range(N):
            for l in range(k + 1, N):
                if k == i or k == j or l == i or l == j:
                    continue

                min_diff = min(min_diff, diff(i, j, k, l))

print(min_diff)