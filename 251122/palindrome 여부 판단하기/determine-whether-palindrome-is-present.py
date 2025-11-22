A = input()

def palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

if palindrome(A):
    print("Yes")
else:
    print("No")