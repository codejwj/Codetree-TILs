MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

min_idx = codenames[0]
min_val = scores[0]

for i in range(MAX_N):
    if scores[i] < min_val:
        min_idx = codenames[i]
        min_val = scores[i]

print(min_idx, min_val)