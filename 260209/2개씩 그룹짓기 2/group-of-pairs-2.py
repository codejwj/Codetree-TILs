import sys

INT_MAX = sys.maxsize

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = INT_MAX
for i in range(N):
    diff = abs(arr[i] - arr[N + i])
    ans = min(ans, diff)

print(ans)