MAX_T = 1000000

N, M = tuple(map(int, input().split()))

pos_A = [0] * (MAX_T + 1)
pos_B = [0] * (MAX_T + 1)

cur_A, time_A = 0, 1
for _ in range(N):
    t1, d1 = tuple(input().split())
    t1 = int(t1)
    for _ in range(t1):
        if d1 == 'L':
            cur_A -= 1
        else:
            cur_A += 1

        pos_A[time_A] = cur_A
        time_A += 1

cur_B, time_B = 0, 1
for _ in range(M):
    t2, d2 = tuple(input().split())
    t2 = int(t2)
    for _ in range(t2):
        if d2 == 'L':
            cur_B -= 1
        else:
            cur_B += 1

        pos_B[time_B] = cur_B
        time_B += 1

total_time = max(time_A, time_B)

for i in range(time_A, total_time + 1):
    pos_A[i] = pos_A[time_A - 1]

for i in range(time_B, total_time + 1):
    pos_B[i] = pos_B[time_B - 1]

ans = 0
for i in range(1, total_time + 1):
    if pos_A[i - 1] != pos_B[i - 1] and pos_A[i] == pos_B[i]:
        ans += 1

print(ans)