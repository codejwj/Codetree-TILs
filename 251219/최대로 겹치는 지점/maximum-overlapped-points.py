N = int(input())
checked = [0] * 101

for _ in range(N):
    x1, x2 = tuple(map(int, input().split()))
    for i in range(x1, x2 + 1):
        checked[i] += 1

print(max(checked))