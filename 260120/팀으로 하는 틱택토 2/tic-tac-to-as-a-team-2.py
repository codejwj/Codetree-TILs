inp = [input() for _ in range(3)]

winning_teams = set()
for i in range(3):
    if len(set(inp[i])) == 2:
        winning_teams.add(tuple(sorted(list(set(inp[i])))))
    if len(set(inp[0][i] + inp[1][i] + inp[2][i])) == 2:
        winning_teams.add(tuple(sorted(list(set(inp[0][i] + inp[1][i] + inp[2][i])))))

if len(set(inp[0][0] + inp[1][1] + inp[2][2])) == 2:
    winning_teams.add(tuple(sorted(list(set(inp[0][0] + inp[1][1] + inp[2][2])))))
if len(set(inp[0][2] + inp[1][1] + inp[2][0])) == 2:
    winning_teams.add(tuple(sorted(list(set(inp[0][2] + inp[1][1] + inp[2][0])))))
        
print(len(winning_teams))