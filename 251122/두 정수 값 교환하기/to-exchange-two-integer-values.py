n, m = tuple(map(int, input().split()))

def swap(x, y):
    x, y = y, x
    return x, y

n, m = swap(n, m)
print(n, m)