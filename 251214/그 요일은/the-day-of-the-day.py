m1, d1, m2, d2 = map(int, input().split())
A = input()

def num_of_days(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    for i in range(1, m):
        total_days += days[i]

    total_days += d
    
    return total_days    

day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

diff = num_of_days(m2, d2) - num_of_days(m1, d1) 

target_idx = day.index(A)
cnt = diff // 7 
remainder = diff % 7

if target_idx <= remainder:
    cnt += 1

print(cnt)