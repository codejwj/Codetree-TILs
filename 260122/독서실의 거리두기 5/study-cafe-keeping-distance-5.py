N = int(input())
seat = list(input())

def min_dist(x):
    arr = []
    for i in range(N):
        if x[i] == '1':
            arr.append(i)
    
    min_val = N
    for j in range(len(arr) - 1):
        val = abs(arr[j] - arr[j + 1])
        min_val = min(min_val, val)

    return min_val
    
ans = 0
for i in range(N):
    if seat[i] == '0':
        seat[i] = '1'
        dist = min_dist(seat)
        seat[i] = '0'
        
        ans = max(ans, dist)

print(ans)