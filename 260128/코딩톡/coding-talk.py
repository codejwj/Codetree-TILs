import sys

N, M, p = tuple(map(int, input().split()))
messages = []

for _ in range(M):
    c, u = input().split()
    messages.append((c, int(u)))

target_unread = messages[p - 1][1]

if target_unread == 0:
    sys.exit()

read_people = set()

for c, u in messages:
    if u >= target_unread:
        read_people.add(c)

for i in range(N):
    name = chr(ord('A') + i)
    if not name in read_people:
        print(name, end = " ")