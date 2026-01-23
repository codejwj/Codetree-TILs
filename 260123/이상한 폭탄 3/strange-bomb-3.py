MAX_NUM = 1000000

N, K = tuple(map(int, input().split()))
num = [
    int(input()) 
    for _ in range(N)
]

bomb = [0] * (MAX_NUM + 1)
explode = [False] * N

maxval = 1
maxidx = 0

for i in range(N):
    for j in range(i + 1, N):
        if j - i > K:
            break

        if num[i] != num[j]:
            continue

        #두 폭탄의 번호가 같을 경우 폭탄은 터짐
        #해당 폭탄이 이미 터진 폭탄인지 확인하고,
        #아직 터지지 않은 폭탄이라면 터진 폭탄의 개수를 갱신
        if explode[i] == False:
            bomb[num[i]] += 1
            explode[i] = True
        
        if explode[j] == False:
            bomb[num[j]] += 1
            explode[j] = True

for i in range(MAX_NUM + 1):
    if maxval <= bomb[i]:
        maxval = bomb[i]
        maxidx = i

print(maxidx)