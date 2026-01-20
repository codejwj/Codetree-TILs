inp = [input() for _ in range(3)]

all_lines = []
all_lines.extend(inp) #가로선 추가
all_lines.extend(zip(*inp)) #세로선 추가
all_lines.append(inp[0][0] + inp[1][1] + inp[2][2]) #대각선1 추가
all_lines.append(inp[0][2] + inp[1][1] + inp[2][0]) #대각선2 추가

#팀 목록을 저장
winning_teams = set()
for line in all_lines:
    s = set(line)
    if len(s) == 2:
        #팀원 2명을 정렬해서 튜플로 만든 뒤 추가(중복 방지)
        winning_teams.add(tuple(sorted(s)))

print(len(winning_teams))