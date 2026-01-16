N, B = tuple(map(int, input().split()))
P = [
    int(input()) 
    for _ in range(N)
]

P.sort()

max_cnt = 0
for i in range(N):
    temp_B = B - (P[i] // 2)
    if temp_B < 0:
        continue

    cnt = 1
    for j in range(N):
        if j == i:
            continue

        if temp_B >= P[j]:
            temp_B -= P[j]
            cnt += 1
        else:
            break

    max_cnt = max(max_cnt, cnt)

print(max_cnt) 