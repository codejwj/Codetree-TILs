N = int(input())
moves = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

cnt1, cnt2 = 0, 0
for x, y in moves:
    if (x, y) == (1, 3) or (x, y) == (2, 1) or (x, y) == (3, 2):
        cnt1 += 1
    elif (x, y) == (1, 2) or (x, y) == (2, 3) or (x, y) == (3, 1):
        cnt2 += 1
        
print(max(cnt1, cnt2))