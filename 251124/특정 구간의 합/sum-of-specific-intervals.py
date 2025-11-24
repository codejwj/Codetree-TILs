N, M = map(int, input().split())
A = list(map(int, input().split()))
a = [tuple(map(int, input().split())) for _ in range(M)]

arr = []

def f():
    global result
    result = []
    
    for i in range(M):
        a1 = a[i][0] - 1
        a2 = a[i][1] - 1

        sum_val = 0

        for j in range(a1, a2 + 1):
            sum_val += A[j]
        
        arr.append(sum_val)

f()
for elem in arr:
    print(elem)