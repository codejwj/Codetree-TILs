A, B = tuple(map(int, input().split()))

def is_prime(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True

sum_val = 0
for i in range(A, B + 1):
    if is_prime(i):
        sum_val += i

print(sum_val)