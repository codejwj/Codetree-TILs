n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)
    
def lcm(a, b):
    return a * b // gcd(a, b)

if not arr:
    lcm_value = 0
else:
    lcm_value = arr[0]

    for i in range(1, n):
        lcm_value = lcm(lcm_value, arr[i])
    
print(lcm_value)