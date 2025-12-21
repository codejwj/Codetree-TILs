CUR = 100000
MAX_R = 200000

N = int(input())
white = [0] * (MAX_R + 1)
black = [0] * (MAX_R + 1)
gray = [0] * (MAX_R + 1)
checked = [0] * (MAX_R + 1)

for _ in range(N):
    X, LR = tuple(input().split())
    X = int(X)
    if LR == 'L':
        for i in range(CUR - X + 1, CUR + 1):
            if gray[i] == 3:
                continue
        
            white[i] += 1
            checked[i] = 1

            if white[i] >= 2 and black[i] >= 2:
                gray[i] = 3

        CUR = CUR - X + 1
    elif LR == 'R':
        for i in range(CUR, CUR + X):
            if gray[i] == 3:
                continue

            black[i] += 1
            checked[i] = 2

            if white[i] >= 2 and black[i] >= 2:
                gray[i] = 3

        CUR = CUR + X - 1

cnt1, cnt2, cnt3 = 0, 0, 0
for i in range(0, MAX_R + 1):
    if gray[i] == 3:
        cnt3 += 1
    elif checked[i] == 1:
        cnt1 += 1
    elif checked[i] == 2:
        cnt2 += 1

print(cnt1, cnt2, cnt3)