N, C, G, H = tuple(map(int, input().split()))
ranges = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

def datasenter(current_temp, T1, T2):
    if current_temp < T1:
        return C
    elif current_temp <= T2:
        return G
    else:
        return H

ans = 0
for T in range(1000):
    sum_val = 0
    for i in range(N):
        T1 = ranges[i][0]
        T2 = ranges[i][1]
        sum_val += datasenter(T, T1, T2)

    ans = max(ans, sum_val)

print(ans)