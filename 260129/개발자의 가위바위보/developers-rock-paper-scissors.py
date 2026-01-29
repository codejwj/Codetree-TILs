N = int(input())
moves = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

cnt1, cnt2 = 0, 0
for x, y in moves:
    if (x, y) in {(1, 3), (2, 1), (3, 2)}:
        cnt1 += 1
    elif (x, y) in {(1, 2), (2, 3), (3, 1)}:
        cnt2 += 1
        
print(max(cnt1, cnt2))