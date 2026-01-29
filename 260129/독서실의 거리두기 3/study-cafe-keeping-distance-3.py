N = int(input())
seats = list(input())

arr = []

for i in range(N):
    if seats[i] == '1':
        arr.append(i)

arr.sort()

max_dist = 0
for i in range(len(arr) - 1):
    max_dist = max(max_dist, arr[i + 1] - arr[i])

    mid = (arr[i + 1] + arr[i]) // 2

    if seats[mid] == '0':
        seats[mid] = '1'
        arr.append(mid)

arr.sort()

ans = 0
for i in range(len(arr) - 1):
    ans = max(ans, arr[i + 1] - arr[i])

print(ans)