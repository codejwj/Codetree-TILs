A, B = tuple(map(int, input().split()))

#3, 6, 9 숫자가 하나라도 포함
def contains_369(x):
    #계속 10으로 나눠 일의 자리를 조사
    while x > 0:
        if x % 10 == 3 or x % 10 == 6 or x % 10 == 9:
            return True
        x //= 10
    
    return False

#3, 6, 9를 포함하거나 3의 배수인지 판단
def is_369_number(x):
    return contains_369(x) or (x % 3 == 0)

cnt = 0
for i in range(A, B + 1):
    if is_369_number(i):
        cnt += 1
    
print(cnt)