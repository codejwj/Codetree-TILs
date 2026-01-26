a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))

def is_overlapping(a, b, c, d):
    if (b < c) or (d < a):
        return 0
    else:
        if (d - a) > (b - c):
            return d - a
        elif c <= b and a <= d:
            return b - c
        elif c <= a and b <= d:
            return d - c

print(is_overlapping(a, b, c, d))