MAX_NUM = 100

N = int(input())
a = list(map(int, input().split()))

ans = -1
min1 = MAX_NUM
min2 = MAX_NUM
idx1 = 0
idx2 = 0

for i in range(N):
    if a[i] < min1:
        min2 = min1
        idx2 = idx1
        min1 = a[i]
        idx1 = i + 1
    elif min1 < a[i] < min2:
        min2 = a[i]
        idx2 = i + 1
        ans = idx2

print(ans)