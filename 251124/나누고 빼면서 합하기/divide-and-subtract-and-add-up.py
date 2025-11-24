N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_val = 0
def f():
    global M 
    global sum_val 
    while M > 0:
        sum_val += A[M - 1]
        M = M // 2

f()
print(sum_val)