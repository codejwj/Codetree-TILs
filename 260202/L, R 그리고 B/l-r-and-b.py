board = [
    list(input()) 
    for _ in range(10)
]

dist = 0
for r in range(10):
    for c in range(10):
        if board[r][c] == 'L':
            L_pos = (r, c)
        elif board[r][c] == 'R':
            R_pos = (r, c)
        elif board[r][c] == 'B':
            B_pos = (r, c)

rL, cL = L_pos
rR, cR = R_pos
rB, cB = B_pos

#맨해튼 거리 계산 (기본 거리 = 행 차이 + 열 차이 - 1 )
dist = abs(rL - rB) + abs(cL - cB) - 1

#세 좌표의 행이 모두 같을 경우 
if rL == rR == rB:
    #R좌표의 열이 두 지점 열 사이에 위치
    if min(cL, cB) < cR < max(cL, cB):
        #위나 아래로 돌아가는 거리 2칸 추가
        dist += 2
#세 좌표의 열이 모두 같을 경우
elif cL == cR == cB:
    #R좌표의 행이 두 지점 행 사이에 위치
    if min(rL, rB) < rR < max(rL, rB):
        #왼쪽이나 오른쪽으로 돌아가는 거리 2칸 추가
        dist += 2

print(dist)