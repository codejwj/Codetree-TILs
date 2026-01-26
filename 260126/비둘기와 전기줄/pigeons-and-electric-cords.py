N = int(input())
arr = []

for _ in range(N):
    p, pos = tuple(map(int, input().split()))
    arr.append((p, pos))

state = [-1] * 11

cnt = 0
for i in range(N):
    p = arr[i][0]
    pos = arr[i][1]

    if state[p] != -1 and state[p] != pos:
        cnt += 1
        
    state[p] = pos

print(cnt)