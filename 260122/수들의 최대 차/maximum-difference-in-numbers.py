N, K = tuple(map(int, input().split()))
arr = [
    int(input()) 
    for _ in range(N)
]

arr.sort()

max_cnt = 0
for i in range(N):
    cnt = 0
    for j in range(i, N):
        if arr[j] - arr[i] <= K:
            cnt += 1
        else:
            break
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)