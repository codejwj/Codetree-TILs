A = input()

def two(x):
    cnt = 0
    for i in range(len(A)):
        if x[i] != x[len(A) - i - 1]:
            cnt += 1
            if cnt >= 2:
                return True

    return False

if two(A):
    print("Yes")
else:
    print("No")