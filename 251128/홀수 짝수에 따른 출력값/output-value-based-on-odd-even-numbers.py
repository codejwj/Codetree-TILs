N = int(input())

def f(n):
    if n == 0:
        return 0
    
    if n % 2 != 0:
        return f(n - 1) + n - 2
    else:
        return f(n - 2) + n
    
print(f(N))