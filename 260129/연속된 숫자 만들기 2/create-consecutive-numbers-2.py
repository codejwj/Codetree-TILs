pos = list(map(int, input().split()))

pos.sort()

#case 1. 3개의 숫자가 전부 연속일 경우
#이 경우에는 이동할 필요가 없으므로 최소 이동 횟수는 0
if pos[1] - pos[0] == 1 and pos[2] - pos[1] == 1:
    print(0)
#case 2. 2개의 숫자의 차이가 정확히 2가 나는 경우
#이 경우에는 남은 숫자를 두 숫자 사이에 바로 넣어주기
#최소 이동 회수는 1
elif pos[1] - pos[0] == 2 or pos[2] - pos[1] == 2:
    print(1)
#case 3. 그렇지 않은 경우에는 항상 2번에 걸쳐
#3개의 숫자를 연속하게 만드는 것이 가능 
else:
    print(2)