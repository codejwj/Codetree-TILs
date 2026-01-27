N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_dist = 0
for i in range(N - 1):
    res = A[i] - B[i]
    total_dist += res
    A[i + 1] += res

print(total_dist)