import sys

INT_MAX = sys.maxsize

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = INT_MAX
#정렬한 뒤 i번째 값과 N + i번째 값의 차이를 구해
#구한 값들 중에서 최솟값을 찾음
for i in range(N):
    diff = arr[N + i] - arr[i]
    ans = min(ans, diff)

print(ans)