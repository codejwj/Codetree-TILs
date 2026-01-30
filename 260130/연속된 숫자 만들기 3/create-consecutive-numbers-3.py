pos = list(map(int, input().split()))

pos.sort()

max_cnt = 0
max_cnt = max(max_cnt, pos[1] - pos[0], pos[2] - pos[1])

print(max_cnt - 1)