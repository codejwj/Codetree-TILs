import sys

INT_MIN = -sys.maxsize

N, K = tuple(map(int, input().split()))
arr = [0] * 20001

for _ in range(N):
    pos, char = input().split()
    pos = int(pos)
    arr[pos] = char

max_score = INT_MIN
for i in range(1, 10001):
    score = 0
    for j in range(i, i + K + 1):
        if arr[j] == 'G':
            score += 1
        elif arr[j] == 'H':
            score += 2

    max_score = max(max_score, score)

print(max_score)