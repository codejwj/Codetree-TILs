a, b = map(int, input().split())

def modify(x, y):
    if x > y:
        x = x + 25
        y = y * 2
    else:
        y = y + 25
        x = x * 2
    return x, y

a, b = modify(a, b)
print(a, b)