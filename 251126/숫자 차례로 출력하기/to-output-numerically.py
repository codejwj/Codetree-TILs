N = int(input())

def f(n):
    if n == 0:
        return

    f(n - 1)
    print(n, end = " ")

def g(n):
    if n == 0:
        return 
    
    print(n, end = " ")
    g(n - 1)

f(N)
print()
g(N)