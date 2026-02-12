import sys

INT_MAX = sys.maxsize

N = int(input())
arr = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

#모든 시작점과 끝점을 각각 분리하여 정렬 
starts = [x[0] for x in arr]
starts.sort() 
ends = [x[1] for x in arr]
ends.sort()

#전체 구간을 결정 짓는 가장 끝값과 그 다음 값을 미리 확보 
min1, min2 = starts[0], starts[1]
max1, max2 = ends[-1], ends[-2]

ans = INT_MAX
for i in range(N):
    #i번째 선분을 지웠다고 가정할 때,
    #남은 선분들의 새로운 시작점과 끝점을 결정 
    new_min = (min2 if arr[i][0] == min1 else min1)
    new_max = (max2 if arr[i][1] == max1 else max1)

    #가장 짧은 선분의 길이를 정답으로 갱신
    ans = min(ans, new_max - new_min)

print(ans)