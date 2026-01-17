MAX_T = 1000

N, C, G, H = tuple(map(int, input().split()))
ranges = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

def performance(t, t1, t2):
    if t < t1:
        return C
    elif t <= t2:
        return G
    else:
        return H

ans = 0
for T in range(MAX_T + 1):
    sum_val = 0
    for i in range(N):
        T1 = ranges[i][0]
        T2 = ranges[i][1]
        sum_val += performance(T, T1, T2)

    ans = max(ans, sum_val)

print(ans)