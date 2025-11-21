A, B = tuple(map(int, input().split()))

def is_onjeonsu(x):
    if x % 2 == 0:
        return False
    elif x % 10 == 5:
        return False
    elif x % 3 == 0 and x % 9 != 0:
        return False
    else:
        return True

cnt = 0
for i in range(A, B + 1):
    if is_onjeonsu(i):
        cnt += 1

print(cnt)