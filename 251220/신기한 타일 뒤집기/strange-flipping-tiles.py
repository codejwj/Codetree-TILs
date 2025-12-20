CUR = 10000
MAX_R = 20000

N = int(input())
checked = [0] * (MAX_R + 1)

for _ in range(N):
    X, LR = tuple(input().split())
    X = int(X)
    if LR == 'L':
        for i in range(CUR - X, CUR):
            checked[i] = 1
        CUR -= X
    elif LR == 'R':
        for i in range(CUR, CUR + X):
            checked[i] = 2
        CUR += X

cnt1, cnt2 = 0, 0
for elem in checked:
    if elem == 1:
        cnt1 += 1
    elif elem == 2:
        cnt2 += 1

print(cnt1, cnt2)