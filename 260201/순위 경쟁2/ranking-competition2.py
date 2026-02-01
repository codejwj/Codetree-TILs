N = int(input())
arr = []

for _ in range(N):
    c, s = input().split()
    s = int(s)
    arr.append((c, s))

cnt = 0
leader = 3
score_A = 0
score_B = 0
for c, s in arr:
    if c == 'A':
        score_A += s
    elif c == 'B':
        score_B += s

    if score_A > score_B:
        if leader != 1:
            cnt += 1
        
        leader = 1
    elif score_A < score_B:
        if leader != 2:
            cnt += 1
        
        leader = 2
    else:
        if leader != 3:
            cnt += 1
        
        leader = 3

print(cnt)