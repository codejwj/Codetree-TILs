N = int(input())
points = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

ans = 0
for x in range(0, 11):
    for y in range(0, 11):
        cnt = 0
        for px, py in points:
            if px == x:
                cnt += 1
            elif py == y:
                cnt += 1
            
            if cnt == 3:
                ans = 1

print(ans)