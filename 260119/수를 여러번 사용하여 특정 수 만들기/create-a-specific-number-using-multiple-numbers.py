MAX_NUM = 1000

A, B, C = tuple(map(int, input().split()))

max_sum = 0
for i in range(0, MAX_NUM + 1):
    sum_val = 0
    for j in range(0, MAX_NUM + 1):
        if A * i + B * j <= C:
            sum_val = A * i + B * j

    max_sum = max(max_sum, sum_val)

print(max_sum)