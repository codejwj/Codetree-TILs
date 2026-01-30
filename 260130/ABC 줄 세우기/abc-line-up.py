N = int(input())
arr = list(input().split())

cnt = 0
for i in range(N):
    #이번 차례에 올 알파벳 결정
    x = chr(ord('A') + i)

    #현재 배열에서 x의 위치를 찾기
    idx = arr.index(x)
    #찾은 위치 idx부터 목표 위치 i까지 역순으로 인접 교환 
    for j in range(idx, i, -1):
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        cnt += 1

print(cnt)