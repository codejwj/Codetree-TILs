A, B = map(int, input().split())

def contains_369(x):
    for digit in str(x):
        if digit in ['3', '6', '9']:
            return True
    return False
    
def is_369_number(x):
    if x % 3 == 0:
        return True
    
    if contains_369(x):
        return True
    
    return False

cnt = 0
for i in range(A, B + 1):
    if is_369_number(i):
        cnt += 1
    
print(cnt)