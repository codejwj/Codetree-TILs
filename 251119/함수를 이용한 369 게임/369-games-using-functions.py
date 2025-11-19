A, B = map(int, input().split())

def find_369(x):
    for n in str(x):
        if n in ['3', '6', '9']:
            return True
    return False
    
def is_magic_number(x):
    if x % 3 == 0:
        return True
    
    if find_369(x):
        return True
    
    return False

cnt = 0
for i in range(A, B + 1):
    if is_magic_number(i):
        cnt += 1
    
print(cnt)