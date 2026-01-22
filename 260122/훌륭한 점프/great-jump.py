MAX_NUM = 100

N, K = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def is_possible(max_val):
    indices = []
    for i, elem in enumerate(arr):
        if elem <= max_val:
            indices.append(i)
    
    arr_size = len(indices)
    for i in range(1, arr_size):
        dist = indices[i] - indices[i - 1]
        if dist > K:
            return False
    
    return True

minimax = MAX_NUM
for a in range(max(arr[0], arr[-1]), max(arr) + 1):
    if is_possible(a):
        minimax = min(minimax, a)
    
print(minimax)