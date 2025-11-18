n = int(input())

def is_magic_number(x):
    original_x = x

    sum_val = 0
    while x > 0:
        sum_val += x % 10
        x //= 10
        
    return original_x % 2 == 0 and sum_val % 5 == 0

if is_magic_number(n):
    print("Yes")
else:
    print("No")