MAX_NUM = 100

N, K = tuple(map(int, input().split()))
arr = [0] * (MAX_NUM + 1)

for _ in range(N):
    candy, x = map(int, input().split())
    arr[x] += candy

max_cnt = 0
for c in range(MAX_NUM):
    cnt = 0
    for i in range(c - K, c + K + 1):
        if i >= 0 and i <= MAX_NUM:
            cnt += arr[i]
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)