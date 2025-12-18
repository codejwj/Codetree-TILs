N, K = map(int, input().split())
blocks = [0] * (N + 1)

for _ in range(K):
    A, B = tuple(map(int, input().split()))
    for i in range(A, B + 1):
        blocks[i] += 1

print(max(blocks))