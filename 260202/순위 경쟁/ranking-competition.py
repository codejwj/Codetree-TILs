N = int(input())
arr = []

for _ in range(N):
    c, s = input().split()
    s = int(s)
    arr.append((c, s))

score_A = score_B = score_C = 0

#명예의 전당 상태를 반환 
def get_status(score1, score2, score3):
    max_score = max(score1, score2, score3)
    
    #각 점수가 최고점과 같은 지 확인(True / False 묶음 반환)
    return (score1 == max_score, score2 == max_score, score3 == max_score)

#처음에는 A, B, C가 모두 0점이기 때문에
#A, B, C 모두 명예의 전당에 올라가 있음
mvp = (True, True, True)
cnt = 0

for c, s in arr:
    if c == 'A':
        score_A += s
    elif c == 'B':
        score_B += s
    else:
        score_C += s
    
    current_state = get_status(score_A, score_B, score_C)
    if current_state != mvp:
        cnt += 1
        mvp = current_state

print(cnt)