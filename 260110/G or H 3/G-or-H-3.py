MAX_NUM = 10000

N, K = tuple(map(int, input().split()))
arr = [0] * (MAX_NUM + 1)

for _ in range(N):
    x, c = input().split()
    x = int(x)
    arr[x] = c

max_sum = 0
for i in range(MAX_NUM - K + 1):
    sum_val = 0
    for j in range(i, i + K + 1):
        if arr[j] == 'G':
            sum_val += 1
        elif arr[j] == 'H':
            sum_val += 2

    max_sum = max(max_sum, sum_val)

print(max_sum)