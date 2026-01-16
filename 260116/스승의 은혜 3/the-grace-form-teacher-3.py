N, B = tuple(map(int, input().split()))
gifts = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

gifts.sort(key = lambda x: x[0] + x[1])

P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

ans = 0
for i in range(N):
    temp_B = B - ((P[i] // 2) + S[i])
    if temp_B < 0:
        continue

    student = 1
    for j in range(N):
        if j == i:
            continue

        if temp_B >= P[j] + S[j]:
            temp_B -= (P[j] + S[j])
            student += 1
        else:
            break
    
    ans = max(ans, student)

print(ans)