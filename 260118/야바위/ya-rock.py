N = int(input())
commands = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

max_score = 0
#시작 위치를 전부 가정
for i in range(1, 4):
    yabawi = [0] * 4
    #i번째 종이컵에 처음 조약돌을 넣고 시작
    yabawi[i] = 1

    score = 0
    for a, b, c in commands:
        #두 종이컵을 교환
        yabawi[a], yabawi[b] = yabawi[b], yabawi[a]

        #교환 이후 c번에 돌이 있다면 점수를 얻음
        if yabawi[c]:
            score += 1
    
    max_score = max(max_score, score)

print(max_score)