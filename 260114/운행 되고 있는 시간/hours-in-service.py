MAX_NUM = 1000

N = int(input())
times = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

ans = 0
for i in range(N):
    count = [0] * (MAX_NUM + 1)
    time = 0
    for j in range(N):
        if j == i:
            continue
        
        A, B = times[j]
        for k in range(A, B):
            count[k] += 1
            if count[k] == 1:
                time += 1

    ans = max(ans, time)

print(ans)