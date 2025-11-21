a, o, c = input().split()
a = int(a)
c = int(c)

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def times(x, y):
    return x * y

def divide(x, y):
    return x // y

if o == '+':
    print(a, o, c, "=", plus(a, c))
elif o == '-':
    print(a, o, c, "=", minus(a, c))
elif o == '*':
    print(a, o, c, "=", times(a, c))
elif o == '/':
    print(a, o, c, "=", divide(a, c))
else:
    print("False")