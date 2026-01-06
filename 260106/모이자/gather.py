import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

N = int(input())
A = list(map(int, input().split()))

min_sum = INT_MAX
for i in range(N):
    sum_val = 0
    for j in range(N):
        sum_val += A[j] * abs(i - j)

    min_sum = min(min_sum, sum_val)

print(min_sum)