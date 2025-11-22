N = int(input())
arr = list(map(int, input().split()))

def modify(x):
    for i in range(N):
        if x[i] % 2 == 0:
            x[i] //= 2

modify(arr)

for elem in arr:
    print(elem, end = " ")