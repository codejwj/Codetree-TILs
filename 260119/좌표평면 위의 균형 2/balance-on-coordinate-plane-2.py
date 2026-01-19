MAX_NUM = 100

N = int(input())
points = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

x_list = list(set([p[0] + 1 for p in points]))
y_list = list(set([p[1] + 1 for p in points]))

ans = MAX_NUM
for x_line in x_list:
    for y_line in y_list:
        q1, q2, q3, q4 = 0, 0, 0, 0
        for px, py in points:
            if px > x_line and py > y_line:
                q1 += 1
            elif px < x_line and py > y_line:
                q2 += 1
            elif px < x_line and py < y_line:
                q3 += 1
            elif px > x_line and py < y_line:
                q4 += 1
            
        M_cnt = max(q1, q2, q3, q4)  
        ans = min(ans, M_cnt)

print(ans)