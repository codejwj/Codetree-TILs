MAX_H = 1000

N = int(input())
H = [
    int(input()) 
    for _ in range(N)
]

max_cnt = 0
for i in range(1, MAX_H + 1):
    cnt = 0
    is_above_water = False
    for j in range(N):
        if H[j] > i:
            if not is_above_water:
                cnt += 1
                is_above_water = True
        else:
            is_above_water = False
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)