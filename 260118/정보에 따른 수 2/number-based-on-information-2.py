MAX_NUM = 1000

T, a, b = tuple(map(int, input().split()))
P = []

for _ in range(T):
    char, pos = tuple(input().split())
    P.append((char, int(pos)))

ans = 0
for k in range(a, b + 1):
    d1 = MAX_NUM
    d2 = MAX_NUM
    for i in range(T):
        if P[i][0] == 'S':
            d1 = min(d1, abs(k - P[i][1]))
        elif P[i][0] == 'N':
            d2 = min(d2, abs(k - P[i][1]))
            
    if d1 <= d2:
        ans += 1

print(ans)