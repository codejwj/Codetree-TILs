N = int(input())
arr = [
    list(map(int, input().split())) 
    for _ in range(N)
]

max_cnt = 0
for i in range(N):
    for j in range(N - 2):
        for k in range(N):
            for l in range(N - 2):
                #두 격자가 겹치는 경우에는 가짓수로 세지 않음
                if i == k and abs(j - l) <= 2:
                    continue

                cnt1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                cnt2 = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                max_cnt = max(max_cnt, cnt1 + cnt2)

print(max_cnt)