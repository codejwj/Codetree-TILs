N = int(input())
arr = list(map(int, input().split()))

def absolute_value(x):
    for i in range(N):
        if x[i] < 0:
            x[i] = -x[i]

absolute_value(arr)

for elem in arr:
    print(elem, end = " ")