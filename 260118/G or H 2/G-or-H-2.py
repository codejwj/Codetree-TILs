N = int(input())
people = []

for _ in range(N):
    x, c = tuple(input().split())
    people.append((int(x), c))

people.sort()

max_size = 0
for i in range(N):
    cnt_G = 0
    cnt_H = 0
    for j in range(i, N):
        if people[j][1] == 'G':
            cnt_G += 1
        else:
            cnt_H += 1

        if cnt_G == 0 or cnt_H == 0 or cnt_G == cnt_H:
            size = people[j][0] - people[i][0]       
            max_size = max(max_size, size)

print(max_size)