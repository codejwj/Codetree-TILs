N = int(input())
seat = list(input())

def min_distance(x):
    arr = []
    min_val = N
    for i in range(N):
        if x[i] == '1':
            arr.append(i)
            
    for j in range(len(arr) - 1):
        val = abs(arr[j] - arr[j + 1])
        min_val = min(min_val, val)

    return min_val
    
max_dist = 0
for i in range(N):
    if seat[i] == '0':
        seat[i] = '1'
        dist = min_distance(seat)
        seat[i] = '0'
        
        max_dist = max(max_dist, dist)

print(max_dist)