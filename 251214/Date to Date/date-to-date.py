m1, d1, m2, d2 = map(int, input().split())
elapsed_days = 1

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if m1 == m2 and d1 == d2:
        break

    elapsed_days += 1
    d1 += 1

    if d1 > num_of_days[m1]:
        m1 += 1
        d1 = 1

print(elapsed_days)