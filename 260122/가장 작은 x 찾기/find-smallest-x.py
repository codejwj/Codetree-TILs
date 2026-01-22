MAX_NUN = 10000

N = int(input())
ranges = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

min_val = MAX_NUN
for x in range(1, MAX_NUN + 1):
    temp_x = x
    is_possible = True
    for i in range(N):
        temp_x *= 2
        a = ranges[i][0]
        b = ranges[i][1]
        if temp_x < a or temp_x > b:
            is_possible = False
            break
    
    if is_possible:
        min_val = min(min_val, x)
    
print(min_val)