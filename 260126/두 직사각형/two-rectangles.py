x1, y1, x2, y2 = tuple(map(int, input().split()))
a1, b1, a2, b2 = tuple(map(int, input().split()))

def overlapping1(x1, x2, a1, a2):
    if (x2 < a1) or (a2 < x1):
        return False
    else:
        return True

def overlapping2(y1, y2, b1, b2):
    if (b2 < y1) or (y2 < b1):
        return False
    else:
        return True

if overlapping1(x1, x2, a1, a2) and overlapping2(y1, y2, b1, b2):
    print("overlapping")
else:
    print("nonoverlapping")