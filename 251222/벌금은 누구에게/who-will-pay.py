N, M, K = tuple(map(int, input().split()))
student = [int(input()) for _ in range(M)]

checked = [0] * (N + 1)

ans = -1
for i in range(M):
    checked[student[i]] += 1
    if checked[student[i]] >= K:
        ans = student[i]
        break

print(ans)