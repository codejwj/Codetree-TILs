N, B = tuple(map(int, input().split()))
gifts = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

gifts.sort(key = lambda x: x[0] + x[1])

ans = 0
for i in range(N):
    temp_B = B - ((gifts[i][0] // 2) + gifts[i][1])
    if temp_B < 0:
        continue

    studnet = 1
    for j in range(N):
        if j == i:
            continue

        if temp_B >= gifts[j][0] + gifts[j][1]:
            temp_B -= (gifts[j][0] + gifts[j][1])
            studnet += 1
        else:
            break
    
    ans = max(ans, studnet)

print(ans)