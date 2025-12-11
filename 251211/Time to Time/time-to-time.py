A, B, C, D = map(int, input().split())
elapsed_time = 0

while True:
    if A == C and B == D:
        break

    elapsed_time += 1
    B += 1

    if B == 60:
        A += 1
        B = 0

print(elapsed_time)