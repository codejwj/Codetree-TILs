N = int(input())
num = list(map(int, input().split()))

max_sum = 0

for i in range(N):
    sum_val = 0
    for j in range(i + 2, N):
        sum_val = num[i] + num[j]
    
    max_sum = max(max_sum, sum_val) 

print(max_sum)