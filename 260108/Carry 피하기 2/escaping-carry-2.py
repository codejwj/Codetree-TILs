N = int(input())
arr = [
    int(input()) 
    for _ in range(N)
]

def is_carry(x, y, z):
    while x > 0 or y > 0 or z > 0:
        if (x % 10) + (y % 10) + (z % 10) >= 10:
            return True
        
        x //= 10
        y //= 10
        z //= 10
    
    return False

max_sum = -1

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if not is_carry(arr[i], arr[j], arr[k]):          
                sum_val = arr[i] + arr[j] + arr[k]
                max_sum = max(max_sum, sum_val)

print(max_sum)