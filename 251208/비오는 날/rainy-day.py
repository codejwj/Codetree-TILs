class Rain:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
rain = [Rain(date, day, weather) for date, day, weather in arr]

idx = 0
for i in range(n):
    if rain[i].weather == "Rain":
        for j in range(i):
            if rain[idx].date < rain[j].date:
                idx = j

print(rain[idx].date, rain[idx].day, rain[idx].weather)