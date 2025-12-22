CUR = 1000000
MAX_T = 2000000

N, M = tuple(map(int, input().split()))

A = [0] * (MAX_T + 1)
B = [0] * (MAX_T + 1)

time = 0
cur = CUR
for _ in range(N):
    d1, t1 = tuple(input().split())
    t1 = int(t1)
    if d1 == 'L':
        for _ in range(t1):
            time += 1
            cur -= 1
            A[time] = cur
    elif d1 == 'R':
        for _ in range(t1):
            time += 1
            cur += 1
            A[time] = cur

time = 0
cur = CUR
for _ in range(M):
    d2, t2 = tuple(input().split())
    t2 = int(t2)
    if d2 == 'L':
        for _ in range(t2):
            time += 1
            cur -= 1
            B[time] = cur
    elif d2 == 'R':
        for _ in range(t2):
            time += 1
            cur += 1
            B[time] = cur

total_time = time

ans = -1
for i in range(1, total_time + 1):
    if A[i] == B[i]:
        ans = i
        break

print(ans)