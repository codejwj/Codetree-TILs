a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))

def intersecting(x1, x2, x3, x4):
    if (x2 < x3) or (x4 < x1):
        return (x2 - x1) + (x4 - x3)
    else:
        return max(x2, x4) - min(x1, x3)

print(intersecting(a, b, c, d))