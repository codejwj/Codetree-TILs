import sys

INT_MAX = sys.maxsize

N = int(input())
A = [int(input()) for _ in range(N)]

min_sum = INT_MAX

for i in range(N):
    sum_dist = 0
    for j in range(N):
        dist = (j - i + N) % N
        sum_dist += A[j] * dist
    
    min_sum = min(min_sum, sum_dist)

print(min_sum)