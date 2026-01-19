A, B, C = tuple(map(int, input().split()))

max_sum = 0
for i in range(C // A + 1):
    sum_val = 0
    for j in range(C // B + 1):
        if A * i + B * j > C:
            break

        sum_val = A * i + B * j

    max_sum = max(max_sum, sum_val)

print(max_sum)