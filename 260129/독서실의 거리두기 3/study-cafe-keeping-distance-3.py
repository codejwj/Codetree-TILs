N = int(input())
seats = list(input())

arr = []

for i in range(N):
    if seats[i] == '1':
        arr.append(i)

max_dist = 0
for i in range(len(arr) - 1):
    dist = arr[i + 1] - arr[i]
    if max_dist <= dist:
        max_dist = dist
        mid = (arr[i + 1] + arr[i]) // 2

if seats[mid] == '0':
    seats[mid] = '1'
    arr.append(mid)

arr.sort()

ans = max_dist // 2
print(ans)