arr = list(map(int, input().split()))
arr.sort()

A = arr[0]
B = arr[1]
C = arr[-1] - A - B

print(A, B, C)