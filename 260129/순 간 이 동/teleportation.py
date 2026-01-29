A, B, x, y = tuple(map(int, input().split()))

#case 1. a -> b 바로 이동
dist1 = abs(A - B)

#case 2. a -> x -> y -> b 순서로 이동
dist2 = abs(A - x) + abs(B - y)

#case 3. a -> y -> x -> b 순서로 이동
dist3 = abs(A - y) + abs(B - x)

print(min(dist1, dist2, dist3))