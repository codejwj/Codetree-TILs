N, M = tuple(map(int, input().split()))
pairs = [
    tuple(map(int, input().split())) 
    for _ in range(M)
]

pairs.sort()

max_cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        cnt = 0
        for a, b in pairs:
            if (a == i and b == j) or (a == j and b == i):
                cnt += 1

        max_cnt = max(max_cnt, cnt)

print(max_cnt)