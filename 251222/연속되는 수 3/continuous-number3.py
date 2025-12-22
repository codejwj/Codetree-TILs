N = int(input())
arr = [int(input()) for _ in range(N)]

cnt = 0
max_cnt = 0

for i in range(N):
    if arr[i] < 0:
        cnt += 1
    else:
        cnt = 0
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)