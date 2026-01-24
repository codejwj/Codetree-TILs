N, L = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0
for h in range(1, N + 1):
    #정답이 h일 때 가능한 지 판단

    #h - 1인 값은 최대 L개까지 h로 올릴 수 있음
    #cnt_h : h 이상인 숫자의 개수(h - 1인 숫자는 L개까지 카운트)
    #cnt_L : 지금까지 1 증가시킨 숫자의 개수
    cnt_h = 0
    cnt_L = 0
    for i in range(N):
        if arr[i] >= h:
            cnt_h += 1
        elif arr[i] == h - 1:
            if cnt_L < L:
                cnt_L += 1
                cnt_h += 1
        
        if cnt_h >= h:
            ans = h
            break
            
print(ans)