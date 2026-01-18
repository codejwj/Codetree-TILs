X, Y = tuple(map(int, input().split()))

def interesting(n):
    s = str(n)
    #set을 이용해 중복 제
    digits = list(set(s))

    #숫자의 종류가 2종류가 아니면 흥미로운 숫자가 아님
    if len(digits) != 2:
        return False
    
    #첫 번째 종류의 숫자 또는 두 번째 종류의 숫자가 한 번만 등장하는가?
    #둘 중 하나라도 개수가 1이면 하나만 다른 숫자 완성
    if s.count(digits[0]) == 1 or s.count(digits[1]) == 1:
        return True
    
    return False

cnt = 0
for i in range(X, Y + 1):
    if interesting(i):
        cnt += 1

print(cnt)