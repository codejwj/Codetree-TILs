N, M = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

max_sum = 0
for i in range(1, N + 1):
    #시작점은 i
    cur = i
    sum_element = 0

    #M번 움직임을 반복
    for _ in range(M):
        sum_element += arr[cur]
        cur = arr[cur]
    
    max_sum = max(max_sum, sum_element)

print(max_sum)