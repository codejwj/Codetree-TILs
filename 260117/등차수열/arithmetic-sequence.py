MAX_NUM = 100

N = int(input())
a = list(map(int, input().split()))

a.sort()

cnt = 0
for i in range(N):
    for j in range(i + 1, N):       
        if (a[i] + a[j]) % 2 == 0:
            cnt += 1

print(cnt)