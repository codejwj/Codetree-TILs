n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0
max_cnt = 0

for i in range(n):
    if i == 0 or arr[i] == arr[i - 1]:
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 1

max_cnt = max(max_cnt, cnt)

print(max_cnt)