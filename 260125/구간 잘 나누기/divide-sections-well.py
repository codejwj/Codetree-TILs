import sys

INT_MAX = sys.maxsize

N, M = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def is_solve(limit):
    if limit < max(arr):
        return False

    cnt = 1
    total = 0
    for num in arr:
        if total + num > limit:
            cnt += 1
            total = num
        else:
            total += num
    
    return cnt <= M

low = max(arr)
high = sum(arr)

ans = INT_MAX
while low <= high:
    mid = (low + high) // 2
    
    if is_solve(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)