N = int(input())
arr = []

for _ in range(N):
    c, s = input().split()
    s = int(s)
    arr.append((c, s))

score_A, score_B = 0, 0

#명예의 전당 상태를 반환
def get_status(score1, score2):
    #case 1. A만 명예의 전당에 올라가 있는 경우
    if score1 > score2:
        return 1
    #case 2. B만 명예의 전당에 올라가 있는 경우
    elif score1 < score2:
        return 2
    #case 3. A, B 모두 명예의 전당에 올라가 있는 경우
    else:
        return 3

#처음에는 A, B가 모두 0점이기 때문에
#A, B 모두 명예의 전당에 올라가 있음
mvp = 3
cnt = 0

for c, s in arr:
    if c == 'A':
        score_A += s
    else:
        score_B += s
    
    current_state = get_status(score_A, score_B)
    if current_state != mvp:
        cnt += 1
        mvp = current_state

print(cnt)