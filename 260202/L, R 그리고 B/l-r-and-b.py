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

dist = abs(rL - rB) + abs(cL - cB) - 1

if rL == rR == rB:
    if min(cL, cB) < cR < max(cL, cB):
        dist += 2
elif cL == cR == cB:
    if min(rL, rB) < rR < max(rL, rB):
        dist += 2

print(dist)