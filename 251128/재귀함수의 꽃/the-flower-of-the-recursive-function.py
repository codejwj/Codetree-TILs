N = int(input())

def print_number(n):
    if n == 0:
        return 

    print(n, end = " ")
    print_number(n - 1)
    print(n, end = " ")

print_number(N)