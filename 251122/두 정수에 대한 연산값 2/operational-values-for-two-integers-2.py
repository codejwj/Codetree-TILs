a, b = tuple(map(int, input().split()))

def change_number(x, y):
    if x < y:
        x = x + 10
        y = y * 2
    else:
        x = x * 2
        y = y + 10
    return x, y

a, b = change_number(a, b)
print(a, b)