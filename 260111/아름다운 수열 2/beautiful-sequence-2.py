N, M = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()

cnt = 0
for i in range(N - M + 1):
    C = A[i : i + M]
    C.sort()
    if C == B:
        cnt += 1

print(cnt)