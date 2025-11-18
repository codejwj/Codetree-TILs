n, m = tuple(map(int, input().split()))

def find_lcm(x, y):
    gcd = 0
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    
    print((x * y) // gcd)

find_lcm(n, m)