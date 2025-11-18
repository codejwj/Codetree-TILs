n = int(input())

def sum_n(x):
    sum_val = 0
    for i in range(1, x + 1):
        sum_val += i

    return sum_val // 10

print(sum_n(n))