class Point:
    def __init__(self, x, y, num):
        self.x, self.y, self.num = x, y, num

n = int(input())
points = []
for i in range(1, n + 1):
    x, y = tuple(map(int, input().split()))
    points.append(Point(x, y, i))

points.sort(key = lambda x: (abs(x.x) + abs(x.y), x.num))

for point in points:
    print(point.num)