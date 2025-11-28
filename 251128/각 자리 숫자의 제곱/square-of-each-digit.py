N = int(input())

def f(n):
    if n < 10:
        return n * n
    
    digit = n % 10
    return f(n // 10) + digit ** 2

print(f(N))