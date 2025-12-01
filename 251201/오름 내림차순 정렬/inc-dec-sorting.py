n = int(input())
nums = list(map(int, input().split()))

nums.sort()
for elem in nums:
    print(elem, end = " ")

print()

for elem in nums[::-1]:
    print(elem, end = " ")