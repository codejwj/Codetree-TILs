import sys

INT_MAX = sys.maxsize

N = int(input())
arr = list(map(int, input().split()))

min_diff = INT_MAX
for i in range(N):
    arr[i] *= 2

    for j in range(N):
        remaining_arr = [elem for k, elem in enumerate(arr) if k != j]

        sum_diff = 0
        for k in range(N - 2):
            sum_diff += abs(remaining_arr[k + 1] - remaining_arr[k])
        
        min_diff = min(min_diff, sum_diff)
    
    arr[i] //= 2

print(min_diff)