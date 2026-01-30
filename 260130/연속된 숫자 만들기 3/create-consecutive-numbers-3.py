pos = list(map(int, input().split()))

pos.sort()

#두 수의 간격 중 큰 값에서 1을 빼면 최대 이동 횟수
#만약 이미 연속된 상태라면 결과는 자동으로 0 
gap1 = pos[1] - pos[0] - 1
gap2 = pos[2] - pos[1] - 1

max_cnt = max(gap1, gap2)
print(max_cnt)