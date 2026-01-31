import sys

INT_MAX = sys.maxsize

N = int(input())
seats = list(input())

arr = []

for i in range(N):
    if seats[i] == '1':
        arr.append(i)

max_dist = 0
pos = 0
left_gap = arr[0]
right_gap = (N - 1) - arr[-1]

if left_gap >= right_gap:
    max_dist = left_gap
    pos = 0
else:
    max_dist = right_gap
    pos = N - 1

for i in range(len(arr) - 1):
    dist = (arr[i + 1] - arr[i]) // 2 
    if dist > max_dist:
        max_dist = dist
        pos = (arr[i + 1] + arr[i]) // 2
    
if seats[pos] == '0':
    seats[pos] = '1'
    arr.append(pos)

arr.sort()

ans = INT_MAX
for i in range(len(arr) - 1):
    ans = min(ans, arr[i + 1] - arr[i])

print(ans)