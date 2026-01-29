A, B, x, y = tuple(map(int, input().split()))

if abs(A - B) < abs(x - y):
    print(abs(A - B))
elif x < y:
    print(abs(A - x) + abs(B - y))
else:
    print(abs(A - y) + abs(B - x))