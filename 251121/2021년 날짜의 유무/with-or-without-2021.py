M, D = tuple(map(int, input().split()))

def day(x, y):
    if x == 2:
        return 1 <= y <= 28
    elif x <= 7:
        if x % 2 == 0:
            return 1 <= y <= 30
        else:
            return 1 <= y <= 31
    elif x <= 12:
        if x % 2 == 0:
            return 1 <= y <= 31
        else:
            return 1 <= y <= 30
    return False

if day(M, D):
    print("Yes")
else:
    print("No")