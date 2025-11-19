y = int(input())

def year(x):
    if x % 4 != 0:
        return False
    if x % 100 == 0 and x % 400 != 0:
        return False
    return True

if year(y):
    print("true")
else:
    print("false")