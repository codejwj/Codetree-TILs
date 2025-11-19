A, B = map(int, input().split())

def diff1(x):
    return x % 10 == 3 or x % 10 == 6 or x % 10 == 9

def diff2(x):
    return x // 10 == 3 or x // 10 == 6 or x // 10 == 9

def is_magic_number(x):
    return x % 3 == 0 or diff1(x) or diff2(x)

cnt = 0
for i in range(A, B + 1):
    if is_magic_number(i):
        cnt += 1
    
print(cnt)