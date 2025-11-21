A, B = tuple(map(int, input().split()))

def is_prime(x):
    if x == 1:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

def is_digit_sum_even(x): 
    digit_sum = (x // 100) + ((x // 10) % 10) + (x % 10)
    if digit_sum % 2 == 0:
        return True
    
    return False

def judge_num(x):
    return is_prime(x) and is_digit_sum_even(x)

cnt = 0
for i in range(A, B + 1):
    if judge_num(i):
        cnt += 1

print(cnt)