a, b = tuple(map(int, input().split()))

def exp(x, y):
    x **= y
    return x

print(exp(a, b))