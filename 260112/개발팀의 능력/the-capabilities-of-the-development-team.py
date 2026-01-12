import sys

INT_MAX = sys.maxsize

N = 5
arr = list(map(int, input().split()))

def diff(x, y, z):
    sum1 = arr[x]
    sum2 = arr[y] + arr[z]
    sum3 = sum(arr) - sum1 - sum2

    #하나라도 합이 같은 팀이 있으면 불가능한 경우
    if sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
        return INT_MAX

    return abs(max(sum1, sum2, sum3) - min(sum1, sum2, sum3))

min_diff = INT_MAX
#첫 번째 팀원 i
for i in range(N):
    #두 번째 팀원 j, k
    for j in range(N):
        for k in range(j + 1, N):
            if i == j or i == k:
                continue

            min_diff = min(min_diff, diff(i, j, k))

if min_diff == INT_MAX:
    print(-1)
else:
    print(min_diff)