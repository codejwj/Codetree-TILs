N, M = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

wifi_cnt = 0
pos = 0

while pos < N:
    if arr[pos] == 1:
        #사람이 있다면 wifi를 설치
        #현재 위치(pos)부터 (pos + 2 * M)까지 사용 가능
        wifi_cnt += 1
        pos = pos + (2 * M) + 1
    else:
        #사람이 없다면 다음 칸으로 이동
        pos += 1

print(wifi_cnt)    