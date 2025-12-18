Y, M, D = tuple(map(int, input().split()))

def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True        
    return False

def is_last_day(y, m):
    if m == 2:
        return 29 if is_leap_year(y) else 28
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def get_season(y, m, d):
    if 1 <= m <= 12 and 1 <= d <= is_last_day(y, m):
        if 3 <= m <= 5:
            return "Spring"
        elif 6 <= m <= 8:
            return "Summer"
        elif 9 <= m <= 11:
            return "Fall"
        else:
            return "Winter"
    else:
        return -1

print(get_season(Y, M, D))