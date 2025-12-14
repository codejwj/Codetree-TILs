A, B, C = map(int, input().split())
day, hour, mins = 11, 11, 11
elapsed_time = 0

if A < day or (A == day and B < hour) or (A == day and B == hour and C < mins):
    print(-1)
else:
    while True:
        if day == A and hour == B and mins == C:
            break

        elapsed_time += 1
        mins += 1

        if mins == 60:
            hour += 1
            mins = 0

            if hour == 24:
                day += 1
                hour = 0
    
    print(elapsed_time)