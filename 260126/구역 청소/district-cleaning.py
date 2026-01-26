a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))

def is_overlapping(a, b, c, d):
    if (b < c) or (d < a):
        return False
    else:
        return True

if b >= c:
    print(b - c)
elif d >= a:
    print(d - a)