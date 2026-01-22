N, K = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def is_possible(limit):
    #마지막 index로부터 숫자 limit을 넘지 않으면서
    #거리 K이내로 계속 이동이 가능한지를 판단
    last_idx = 0
    for i in range(1, N):
        if arr[i] <= limit:
            if i - last_idx > K:
                return False
            last_idx = i
    
    return True

#밟으며 지나간 최댓값을 i라고 가정
#거리 K이내로 점프하며 끝까지 도달하는 것이 가능한지를 살펴봄
#가능하다면, 그때의 i가 최솟값이므로 답을 출력하고 종료
for i in range(max(arr[0], arr[N - 1]), max(arr) + 1):
    if is_possible(i):
        print(i)
        break