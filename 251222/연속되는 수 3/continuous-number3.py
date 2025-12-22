N = int(input())
arr = [int(input()) for _ in range(N)]

cnt1 = 0
cnt2 = 0
max_cnt = 0

for i in range(N):
    if arr[i] > 0:
        cnt1 += 1
        cnt2 = 0
    elif arr[i] < 0:
        cnt2 += 1
        cnt1 = 0
    
    max_cnt = max(max_cnt, cnt1, cnt2)

print(max_cnt)