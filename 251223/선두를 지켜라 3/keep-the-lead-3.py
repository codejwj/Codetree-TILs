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

#A가 리더면 1, B가 리더면 2, 둘 다 리더면 3
leader, cnt = 0, 0
for i in range(1, len(pos_A)):
    if pos_A[i] > pos_B[i]:
        #조합이 바뀌었다면 답을 갱신
        if leader != 1:
            cnt += 1
        #리더 A
        leader = 1
    elif pos_A[i] < pos_B[i]:
        #조합이 바뀌었다면 답을 갱신
        if leader != 2:
            cnt += 1
        #리더 B
        leader = 2
    else:
        #조합이 바뀌었다면 답을 갱신
        if leader != 3:
            cnt += 1
        #둘 다 리더
        leader = 3
        
print(cnt)