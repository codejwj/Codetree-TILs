A, B = map(int, input().split())

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False

    return True

sum_val = 0
for i in range(A, B + 1):
    if is_prime(i):
        sum_val += i

print(sum_val)