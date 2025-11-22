a, b = tuple(map(int, input().split()))

def change_number(x, y):
    if x > y:
        x = x + 25
        y = y * 2
    else:
        y = y + 25
        x = x * 2
    return x, y

a, b = change_number(a, b)
print(a, b)