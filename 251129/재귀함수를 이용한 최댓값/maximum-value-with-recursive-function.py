N = int(input())
arr = list(map(int, input().split()))

def f(n):
    if n == 1:
        return arr[1]
    
    return max(f(n - 1), arr[n - 1])

print(f(N))