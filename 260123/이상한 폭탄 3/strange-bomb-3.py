N, K = tuple(map(int, input().split()))
num = [
    int(input()) 
    for _ in range(N)
]

ans = 0
for i in range(N):
    cnt = 0
    for j in range(i + 1, N):
        if j - i > K:
            break

        if num[i] != num[j]:
            continue
        else:
            cnt += 1
        
        if max(0, cnt):
            ans = num[i]
    
print(ans)