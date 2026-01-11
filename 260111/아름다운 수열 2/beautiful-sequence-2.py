N, M = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(N - M + 1):
    if sorted(A[i : i + M]) == sorted(B):
        cnt += 1

print(cnt)