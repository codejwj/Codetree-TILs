X, Y = tuple(map(int, input().split()))

def interesting(n):
    s = str(n)
    digits = list(set(s))

    if len(digits) != 2:
        return False
    
    if s.count(digits[0]) == 1 or s.count(digits[1]) == 1:
        return True
    
    return False

cnt = 0
for i in range(X, Y + 1):
    if interesting(i):
        cnt += 1

print(cnt)