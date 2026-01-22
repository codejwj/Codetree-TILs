import sys

MAX_NUM = 40

nums = list(map(int, input().split()))
nums.sort()

for A in range(1, MAX_NUM + 1):
    for B in range(A, MAX_NUM + 1):
        for C in range(B, MAX_NUM + 1):
            for D in range(C, MAX_NUM + 1):
                list = [A, B, C, D, A + B, B + C, C + D, D + A, A + C, B + D, A + B + C, A + B + D, A + C + D, B + C + D, A + B + C + D]
                if sorted(list) == nums:
                    print(A, B, C, D)
                    sys.exit()