A = input()
B = input()

def find_index():
    N = len(A)
    M = len(B)
    for i in range(N - M + 1):
        if A[i : i + M] == B:
            return i
    
    return -1

print(find_index())