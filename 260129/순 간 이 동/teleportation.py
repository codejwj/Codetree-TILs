A, B, x, y = tuple(map(int, input().split()))

dist1 = abs(A - B)
dist2 = abs(A - x) + abs(B - y)
dist3 = abs(A - y) + abs(B - x)

print(min(dist1, dist2, dist3))