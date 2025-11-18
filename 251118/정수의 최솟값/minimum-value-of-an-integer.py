a, b, c = tuple(map(int, input().split()))

def get_min(x, y, z):
    return min(x, y, z)

print(get_min(a, b, c))