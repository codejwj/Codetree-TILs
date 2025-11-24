N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_val = 0
def f():
    global M 
    global sum_val 
    while M >= 1:
        sum_val += A[M - 1]
        
        if M % 2 != 0:
            M -= 1
        else:
            M //= 2

f()
print(sum_val)