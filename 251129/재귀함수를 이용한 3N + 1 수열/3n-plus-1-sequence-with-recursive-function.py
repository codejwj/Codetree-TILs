N = int(input())

def f(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return f(n // 2) + 1
    else:
        return f(n * 3 + 1) + 1

print(f(N))