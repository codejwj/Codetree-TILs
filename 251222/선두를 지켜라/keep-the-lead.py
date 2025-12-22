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

#A가 리더면 1, B가 리더면 2로 설정
leader, cnt = 0, 0
for i in range(1, len(pos_A)):
    if pos_A[i] > pos_B[i]:
        #기존 리더가 B라면 횟수를 갱신
        if leader == 2:
            cnt += 1
        #리더를 A로 변경
        leader = 1
    elif pos_A[i] < pos_B[i]:
        #기존 리더가 A라면 횟수를 갱신
        if leader == 1:
            cnt += 1
        #리더를 B로 변경
        leader = 2

print(cnt)  