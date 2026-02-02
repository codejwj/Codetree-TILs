n = int(input())
a = list(map(int, input().split()))

pos = list(set(a))
pos.sort()

if len(pos) < 2:
    print(-1)
elif a.count(pos[1]) >= 2:
    print(-1)
else:
    print(a.index(pos[1]) + 1)