A, B = map(int, input().split())

def is_prime(x):
    if x == 1:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

def even_sum(x):
    return is_prime(x) and (x // 10 + (x % 10)) % 2 == 0

cnt = 0
for i in range(A, B + 1):
    if even_sum(i):
        cnt += 1

print(cnt)