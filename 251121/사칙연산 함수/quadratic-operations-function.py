a, o, c = input().split()
a = int(a)
c = int(c)

def add(x, y):
    return(f"{x} + {y} = {x + y}")

def sub(x, y):
    return(f"{x} - {y} = {x - y}")

def multi(x, y):
    return(f"{x} * {y} = {x * y}")

def div(x, y):
    return(f"{x} / {y} = {x // y}")

if o == '+':
    print(add(a, c))
elif o == '-':
    print(sub(a, c))
elif o == '*':
    print(multi(a, c))
elif o == '/':
    print(div(a, c))
else:
    print("False")