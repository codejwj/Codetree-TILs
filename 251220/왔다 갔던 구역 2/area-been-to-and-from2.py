CUR = 1000
MAX_R = 2000

N = int(input())
checked = [0] * (MAX_R + 1)

for _ in range(N):
    X, LR = tuple(input().split())
    X = int(X)
    if LR == 'L':
        for i in range(CUR - X, CUR):
            checked[i] += 1
        CUR -= X
    elif LR == 'R':
        for i in range(CUR, CUR + X):
            checked[i] += 1
        CUR += X

cnt = 0
for elem in checked:
    if elem >= 2:
        cnt += 1

print(cnt)