N, B = tuple(map(int, input().split()))
P = [
    int(input()) 
    for _ in range(N)
]

P.sort()

ans = 0
for i in range(N):
    temp_B = B - (P[i] // 2)
    if temp_B < 0:
        continue

    student = 1
    for j in range(N):
        if j == i:
            continue

        if temp_B >= P[j]:
            temp_B -= P[j]
            student += 1
        else:
            break

    ans = max(ans, student)

print(ans) 