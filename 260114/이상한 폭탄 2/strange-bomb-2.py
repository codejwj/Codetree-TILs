N, K = tuple(map(int, input().split()))
num = [
    int(input()) 
    for _ in range(N)
]

max_num = -1
for i in range(N):
    for j in range(i + 1, N):
        #거리가 K를 초과하는 경우 넘어감
        if j - i > K:
            break 

        #두 폭탄의 번호가 다를 경우 터지지 않음
        if num[i] != num[j]:
            continue
        
        max_num = max(max_num, num[i])

print(max_num)