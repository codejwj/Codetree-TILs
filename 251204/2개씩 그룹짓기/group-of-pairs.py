N = int(input())
nums = list(map(int, input().split()))

#nums 정렬
nums.sort()

max_val = 0
for i in range(N):
    sum_val = nums[i] + nums[-(i + 1)]
    if sum_val > max_val:
        max_val = sum_val

print(max_val)