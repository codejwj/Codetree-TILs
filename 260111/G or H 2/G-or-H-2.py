N = int(input())
people = []

for _ in range(N):
    x, c = input().split()
    people.append((int(x), c))

people.sort()

max_size = 0
for i in range(N):
    cnt1 = 0
    cnt2 = 0
    for j in range(i, N):
        if people[j][1] == 'G':
            cnt1 += 1
        else:
            cnt2 += 1

        if cnt1 == 0 or cnt2 == 0 or cnt1 == cnt2:
            size = people[j][0] - people[i][0]       
            max_size = max(max_size, size)

print(max_size)