N, K, T = input().split()
N, K = int(N), int(K)
str = [input() for _ in range(N)]

str.sort()

cnt = 0
for i in range(N):
    if T in str[i]:
        cnt += 1
        if cnt == K:
            print(str[cnt])
            break