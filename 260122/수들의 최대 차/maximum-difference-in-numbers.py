MAX_NUM = 10000

N, K = tuple(map(int, input().split()))
arr = [
    int(input()) 
    for _ in range(N)
]

max_cnt = 0
for n in range(1, MAX_NUM + 1):
    cnt = 0
    for elem in arr:
        if abs(elem - n) < K:
            cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)