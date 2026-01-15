K, N = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split())) 
    for _ in range(K)
]

cnt = 0
for a in range(N):
    for b in range(N):
        if a == b:
            continue
        
        win = True
        for i in range(K):
            if arr[i][a] >= arr[i][b]:
                win = False
                break

        if win:
            cnt += 1
    
print(cnt)