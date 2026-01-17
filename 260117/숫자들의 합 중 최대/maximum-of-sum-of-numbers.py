X, Y = tuple(map(int, input().split()))

max_sum = 0
for i in range(X, Y + 1):
    d1, d2 = tuple(map(int, list(str(i))))
    sum_val = d1 + d2
    max_sum = max(max_sum, sum_val)

print(max_sum)