CUR = 1000

N = int(input())
checked = [0] * 2001

cnt = 0
for _ in range(N):
    X, LR = input().split()
    X = int(X)
    if LR == "L":
        for i in range(CUR - X, CUR):
            checked[i] += 1
        CUR -= X
    elif LR == "R":
        for i in range(CUR, CUR + X):
            checked[i] += 1
        CUR += X

ans = 0
for val in checked:
    if val >= 2:
        ans += 1

print(ans)