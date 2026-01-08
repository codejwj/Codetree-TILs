import sys

INT_MIN = -sys.maxsize

a = list(map(int, list(input())))

max_val = INT_MIN
for i in range(len(a)):
    a[i] = 1 - a[i]
    num = 0
    for j in range(len(a)):
        num = num * 2 + a[j]
        
    max_val = max(max_val, num)
    a[i] = 1 - a[i]

print(max_val)