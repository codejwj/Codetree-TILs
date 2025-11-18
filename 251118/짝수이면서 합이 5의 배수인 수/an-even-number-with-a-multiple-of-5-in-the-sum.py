n = int(input())

def is_magic_number(x):
    return x % 2 == 0 and (x // 10 + (x % 10)) % 5 == 0

if is_magic_number(n):
    print("Yes")
else:
    print("No")