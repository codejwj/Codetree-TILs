N = int(input())
checked = [0] * 201

for _ in range(N):
    x1, x2 = tuple(map(int, input().split()))
    for i in range(x1 + 100, x2 + 100):
        checked[i] += 1

print(max(checked))