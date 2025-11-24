N, M = map(int, input().split())
A = list(map(int, input().split()))


def get_answer():
    global M 
    sum_val = 0
    while M >= 1:
        sum_val += A[M - 1]
        
        if M % 2 != 0:
            M -= 1
        else:
            M //= 2
    
    return sum_val

print(get_answer())