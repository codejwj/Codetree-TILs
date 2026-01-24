MAX_NUM = 100

N, L = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0
for num in range(1, N + 1):
    cnt_H = 0
    cnt_L = 0
    for i in range(N):
        if arr[i] >= num:
            cnt_H += 1
        elif arr[i] == num - 1:
            if cnt_L < L:
                cnt_L += 1
                cnt_H += 1
        
        if cnt_H >= num:
            ans = num
            break

print(ans)