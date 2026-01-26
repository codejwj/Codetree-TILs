N = int(input())
movements = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

#현재 비둘기의 위치를 기록
#-1이면 아직 미정인 상태
pos = [-1] * 11

move_cnt = 0
for pigeon, move_dir in movements:
    #해당 비둘기의 위치가 미정이 아니고 옮겨간 위치와 다른 위치라면 
    #이동 횟수 증가
    if pos[pigeon] != -1 and pos[pigeon] != move_dir:
        move_cnt += 1

    pos[pigeon] = move_dir

print(move_cnt)