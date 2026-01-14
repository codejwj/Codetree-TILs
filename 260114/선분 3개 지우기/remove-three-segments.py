MAX_NUM = 100

N = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

def get_max_overlapped_cnt(x, y, z):
    count = [0] * (MAX_NUM + 1)
    for i in range(N):
        if i in [x, y, z]:
            continue
        
        x1, x2 = arr[i]
        for j in range(x1, x2 + 1):
            count[j] += 1
        
    return max(count)

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            max_cnt = get_max_overlapped_cnt(i, j, k)

            if max_cnt <= 1:
                cnt += 1

print(cnt)