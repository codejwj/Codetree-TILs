N = int(input())
moves = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

max_score = 0
for pos in [1, 2, 3]:
    current_pos = pos
    score = 0

    for a, b, c in moves:
        if current_pos == a:
            current_pos = b
        elif current_pos == b:
            current_pos = a
        
        if current_pos == c:
            score += 1
    
    max_score = max(max_score, score)

print(max_score)