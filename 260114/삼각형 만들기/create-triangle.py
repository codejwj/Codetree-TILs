N = int(input())
points = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

def tri(i, j, k):
    x1, y1 = points[i]
    x2, y2 = points[j]
    x3, y3 = points[k]
    
    if x1 == x2 and y1 == y3:
        return abs(x3 - x1) * abs(y2 - y1)
    if x1 == x3 and y1 == y2:
        return abs(x2 - x1) * abs(y3 - y1)
    
    if x2 == x1 and y2 == y3:
        return abs(x3 - x2) * abs(y1 - y2)
    if x2 == x3 and y2 == y1:
        return abs(x1 - x2) * abs(y3 - y2)

    if x3 == x1 and y3 == y2:
        return abs(x2 - x3) * abs(y1 - y3)
    if x3 == x2 and y3 == y1:
        return abs(x1 - x3) * abs(y2 - y3)
    
    return 0

max_size = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            max_size = max(max_size, tri(i, j, k))
        
print(max_size)