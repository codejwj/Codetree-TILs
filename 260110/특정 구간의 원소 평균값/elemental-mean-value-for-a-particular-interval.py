N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(N):
    sum = 0
    avg = 0
    for j in range(i, N):
        sum += arr[j]

        if sum % (j + 1 - i) == 0:
            avg = sum // (j + 1 - i)

            if avg in arr[i : j + 1]:
                cnt += 1

print(cnt)