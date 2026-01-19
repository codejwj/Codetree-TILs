N, M = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

max_sum = 0
for i in range(1, N + 1):
    current_pos = i
    sum_val = 0
    for j in range(1, M + 1):
        elem = arr[current_pos]        
        sum_val += elem
        current_pos = elem
    
    max_sum = max(max_sum, sum_val)

print(max_sum)