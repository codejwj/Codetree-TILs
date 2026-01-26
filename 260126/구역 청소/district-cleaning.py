a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))

def is_area(a, b, c, d):
    if (b < c) or (d < a):
        return (b - a) + (d - c)
    else:
        return max(b, d) - min(a, c)

print(is_area(a, b, c, d))