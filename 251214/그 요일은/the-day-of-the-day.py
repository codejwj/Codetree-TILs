m1, d1, m2, d2 = map(int, input().split())
A = input()

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_days = [0]

for i in range(12):
    sum_days.append(sum_days[i] + num_of_days[i + 1])

day_1 = sum_days[m1 - 1] + d1
day_2 = sum_days[m2 - 1] + d2
N = day_2 - day_1 + 1

day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

start_idx = (day_1 - 1) % 7
target_idx = day.index(A)

cnt = N // 7
r = N % 7
if r > 0:
    for i in range(r):
        if (start_idx + i) % 7 == target_idx:
            cnt += 1
            break

print(cnt)