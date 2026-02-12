MAX_NUM = 100

N = int(input())
arr = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

starts = [x[0] for x in arr]
starts.sort() 
ends = [x[1] for x in arr]
ends.sort()

min1, min2 = starts[0], starts[1]
max1, max2 = ends[-1], ends[-2]

ans = MAX_NUM
for i in range(N):
    new_min = (min2 if arr[i][0] == min1 else min1)
    new_max = (max2 if arr[i][1] == max1 else max1)

    ans = min(ans, new_max - new_min)

print(ans)