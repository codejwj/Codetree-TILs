A = input()

def is_more_twoalp(x):
    for i in range(len(x)):
        if x[i] != x[0]:
            return True

    return False

if is_more_twoalp(A):
    print("Yes")
else:
    print("No")