class Rain:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
rain = [Rain(date, day, weather) for date, day, weather in arr]

idx = None
for i in range(n):
    if rain[i].weather == "Rain":
        if idx is None:
            idx = i
        elif rain[i].date < rain[idx].date:
            idx = i

print(rain[idx].date, rain[idx].day, rain[idx].weather)