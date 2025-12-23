N, M = tuple(map(int, input().split()))

pos_A = [0]
pos_B = [0]

for _ in range(N):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_A.append(pos_A[-1] + v)
    
for _ in range(M):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_B.append(pos_B[-1] + v)

leader, cnt = 0, 0
for i in range(0, len(pos_A)):
    if pos_A[i] > pos_B[i]:
        cur_leader = 1
    elif pos_A[i] < pos_B[i]:
        cur_leader = 2
    elif pos_A[i] == pos_B[i]:
        cur_leader = 3

    if leader == 0:
        leader = cur_leader
        continue
    
    if leader != cur_leader:
        cnt += 1
        leader = cur_leader

print(cnt)