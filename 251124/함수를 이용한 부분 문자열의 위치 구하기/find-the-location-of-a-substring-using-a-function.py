A = input()
B = input()

def text_index(x, y):
    N = len(x)
    M = len(y)
    for i in range(N - M + 1):
        if x[i : i + M] == y:
            return i
    
    return -1

print(text_index(A, B))