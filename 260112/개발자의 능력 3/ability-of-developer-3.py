import sys

INT_MAX = sys.maxsize

abilities = list(map(int, input().split()))

def get_diff(x, y, z):
    sum1 = abilities[x] + abilities[y] + abilities[z]
    sum2 = sum(abilities) - sum1
    return abs(sum1 - sum2)

min_diff = INT_MAX
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            min_diff = min(min_diff, get_diff(i, j, k))

print(min_diff)