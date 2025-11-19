y = int(input())

def is_leap_year(x):
    if x % 4 != 0:
        return False
    if x % 100 == 0 and x % 400 != 0:
        return False
    return True

if is_leap_year(y):
    print("true")
else:
    print("false")