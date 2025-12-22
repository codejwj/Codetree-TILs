N, T = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
max_cnt = 0

for i in range(N):
    if arr[i] > T:
        cnt += 1
    else:
        cnt = 0

    max_cnt = max(max_cnt, cnt)

print(max_cnt)