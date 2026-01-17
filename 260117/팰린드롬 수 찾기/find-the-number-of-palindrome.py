X, Y = tuple(map(int, input().split()))

def palindrome_num(n):
    l = len(str(n))
    num = list(str(n))
    for i in range(l // 2):
        if num[i] != num[l - 1 - i]:
            return False
    
    return True

cnt = 0
for i in range(X, Y + 1):
    if palindrome_num(i):
        cnt += 1

print(cnt)