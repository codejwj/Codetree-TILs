import sys

MAX_NUM = 100

arr = list(map(int, input().split()))
arr.sort()

for A in range(1, MAX_NUM):
    for B in range(A, MAX_NUM):
        for C in range(B, MAX_NUM):
            list = [A, B, C, A + B, B + C, C + A, A + B + C]
            if sorted(list) == arr:
                print(A, B, C)
                sys.exit()