n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def is_consecutive_subarray(x, y):
    n1 = len(x)
    n2 = len(y)
    for i in range(n1 - n2 + 1):
        subarray = x[i : i + n2]
        if subarray == y:
            return True

    return False

if is_consecutive_subarray(A, B):
    print("Yes")
else:
    print("No")