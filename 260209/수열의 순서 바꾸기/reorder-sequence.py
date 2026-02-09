N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(N):
    satisfied = False
    for j in range(i, N - 1):
        if arr[j] > arr[j + 1]:
            satisfied = True
            break

    if satisfied:
        cnt += 1

print(cnt)