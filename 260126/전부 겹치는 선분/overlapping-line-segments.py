MAX_NUM = 100

N = int(input())
segments = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

max_start = 0
min_end = MAX_NUM

flag = True
for x1, x2 in segments:
    max_start = max(max_start, x1)
    min_end = min(min_end, x2)
    
    if max_start > min_end:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")