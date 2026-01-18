import sys

INT_MAX = sys.maxsize

T, a, b = tuple(map(int, input().split()))
sn_data = [
    tuple(input().split())
    for _ in range(T)
]

ans = 0
for k in range(a, b + 1):
    d1 = INT_MAX
    d2 = INT_MAX
    for char, pos in sn_data:
        pos = int(pos)

        if char == 'S':
            d1 = min(d1, abs(k - pos))
        elif char == 'N':
            d2 = min(d2, abs(k - pos))
            
    if d1 <= d2:
        ans += 1

print(ans)