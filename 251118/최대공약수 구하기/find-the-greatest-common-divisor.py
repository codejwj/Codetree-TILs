n, m = tuple(map(int, input().split()))

def find_gcd(x, y):
    gcd = 0
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
            
    print(gcd)

find_gcd(n, m)