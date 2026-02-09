N = int(input())
blocks = [
    int(input()) 
    for _ in range(N)
]

total = sum(blocks)
avg = total // N

ans = 0
for i in range(N):
    if blocks[i] > avg:
        ans += (blocks[i] - avg)

print(ans)