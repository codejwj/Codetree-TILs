import sys

INT_MAX = sys.maxsize

N = int(input())
A = list(map(int, input().split()))

min_dist = INT_MAX
#각 i번째 집으로 모였을 때의 합을 계산
for i in range(N):
    sum_dist = 0
    for j in range(N):
        sum_dist += A[j] * abs(j - i)

    #가능한 거리의 합 중 최솟값을 구함
    min_dist = min(min_dist, sum_dist)

print(min_dist)