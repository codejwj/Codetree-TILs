x1, y1, x2, y2 = tuple(map(int, input().split()))
a1, b1, a2, b2 = tuple(map(int, input().split()))

w = max(x2, a2) - min(x1, a1)
h = max(y2, b2) - min(y1, b1)

print(w * h)