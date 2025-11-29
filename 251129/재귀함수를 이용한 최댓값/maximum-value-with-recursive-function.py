N = int(input())
arr = list(map(int, input().split()))

def f(n):
    if n == 0:
        return arr[0]
    
    return max(f(n - 1), arr[n - 1])

print(f(N))