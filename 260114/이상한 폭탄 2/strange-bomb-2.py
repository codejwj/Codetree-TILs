N, K = tuple(map(int, input().split()))
num = [
    int(input()) 
    for _ in range(N)
]

max_num = -1
for i in range(N):
    for j in range(i + 1, min(i + K + 1, N)):
        if num[i] == num[j]:
            max_num = max(max_num, num[i])

print(max_num)