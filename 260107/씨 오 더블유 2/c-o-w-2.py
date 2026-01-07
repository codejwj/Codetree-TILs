N = int(input())
S = input()

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if S[i] == 'C' and S[j] == 'O' and S[k] == 'W':
                cnt += 1

print(cnt)