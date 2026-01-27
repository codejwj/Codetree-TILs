N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

#마지막 집은 사람을 보낼 곳이 없으므로 N - 1까지 설정
for i in range(N - 1):
    if A[i] > B[i]:
        num = A[i] - B[i]
        #현재 집 인원을 B[i]로 맞춤
        A[i] -= num
        #다음 집으로 인원 이동
        A[i + 1] += num
        ans += num

print(ans)