n = int(input())

def sub(x):
    sum_val = 0
    for i in range(1, x + 1):
        sum_val += i
    return sum_val // 10

n = sub(n)
print(n)