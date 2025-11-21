M, D = tuple(map(int, input().split()))

def last_day_number(x):
    if x == 2:
        return 28
    elif x == 4 or x == 6 or x == 9 or x == 11:
        return 30
    else:
        return 31

def judge_day(x, y):
    if x <= 12 and y <= last_day_number(x):
        return True
    
    return False

if judge_day(M, D):
    print("Yes")
else:
    print("No")