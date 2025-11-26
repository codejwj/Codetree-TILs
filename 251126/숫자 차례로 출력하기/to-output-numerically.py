N = int(input())

def print_number1(n):
    if n == 0:
        return

    print_number1(n - 1)
    print(n, end = " ")

def print_number2(n):
    if n == 0:
        return 
    
    print(n, end = " ")
    print_number2(n - 1)

print_number1(N)
print()
print_number2(N)