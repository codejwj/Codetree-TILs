MAX_NUM = 100

N = int(input())
a = list(map(int, input().split()))

a.sort()

max_cnt = 0
for K in range(1, MAX_NUM + 1):
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):       
            if a[j] - K == K - a[i]:
                cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)