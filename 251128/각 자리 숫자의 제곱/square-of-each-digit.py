N = int(input())

def f(n):
    if n < 10:
        return n * n
    
    return f(n // 10) + (n % 10) * (n % 10)

print(f(N))