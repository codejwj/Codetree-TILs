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
        #K번의 모든 경기에 대해서 두 개발자의 위치를 찾음
        #하나라도 a번 개발자가 b번 개발자보다 뒤에 있으면 False로 변경
        for i in range(K):
            rank_a = arr[i].index(a)
            rank_b = arr[i].index(b)

            if rank_a > rank_b:
                is_always_better = False
                break

        if is_always_better:
            cnt += 1
    
print(cnt)