N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(N - 2, -1, -1):
    #뒤에서부터 탐색하며 정렬이 깨지는 마지막 위치를 찾아
    #그 앞의 모든 원소를 이동 횟수로 계산
    if arr[i] > arr[i + 1]:
        cnt = i + 1
        break

print(cnt)