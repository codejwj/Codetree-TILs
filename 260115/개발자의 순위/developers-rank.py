K, N = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split())) 
    for _ in range(K)
]

cnt = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            continue
        
        is_always_better = True
        for i in range(K):
            rank_a = arr[i].index(a)
            rank_b = arr[i].index(b)

            if rank_a > rank_b:
                is_always_better = False
                break

        if is_always_better:
            cnt += 1
    
print(cnt)