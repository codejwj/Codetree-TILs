N = int(input())
nums = list(map(int, input().split()))

nums.sort()
sum_val = 0
result = []

for i in range(2 * N):
    sum_val = nums[i] + nums[-(i + 1)]
    result.append(sum_val)

print(max(result))