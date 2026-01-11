MAX_NUM = 200

N, K = tuple(map(int, input().split()))
arr = [0] * (MAX_NUM + 1)

for _ in range(N):
    candy, x = map(int, input().split())
    arr[x] += candy

max_cnt = 0
for c in range(MAX_NUM - K + 1):
    cnt = 0
    start = max(0, c - K)
    end = min(MAX_NUM, c+ K)
    for i in range(start, end + 1):
        cnt += arr[i]
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)