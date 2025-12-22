N, M = tuple(map(int, input().split()))

pos_A = [0] 
pos_B = [0]

v, t = 0, 0
for _ in range(N):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_A.append(pos_A[-1] + v)

v, t = 0, 0
for _ in range(M):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_B.append(pos_B[-1] + v) 

leader = 0
cnt = 0
for i in range(1, len(pos_A)):
    if pos_A[i] > pos_B[i]:
        if leader == 2:
            cnt += 1
        leader = 1
    elif pos_A[i] < pos_B[i]:
        if leader == 1:
            cnt += 1
        leader = 2

print(cnt)  