x1, y1, x2, y2 = tuple(map(int, input().split()))
a1, b1, a2, b2 = tuple(map(int, input().split()))

def is_overlapping(start1, start2, end1, end2):
    if (start2 < end1) or (end2 < start1):
        return False
    else:
        return True

if is_overlapping(x1, x2, a1, a2) and is_overlapping(y1, y2, b1, b2):
    print("overlapping")
else:
    print("nonoverlapping")