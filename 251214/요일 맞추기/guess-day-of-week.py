m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_days = [0]

for i in range(12):
    sum_days.append(sum_days[i] + num_of_days[i + 1])

day_1 = sum_days[m1 - 1] + d1
day_2 = sum_days[m2 - 1] + d2

day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

diff = (day_2 - day_1) % 7
print(day[diff])