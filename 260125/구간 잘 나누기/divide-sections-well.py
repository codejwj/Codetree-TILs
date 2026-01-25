MAX_A = 10000

N, M = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = MAX_A
#구간의 합의 최댓값이 a일 때
for a in range(1, MAX_A + 1):
    #possible : 구간을 나눌 수 있으면 True
    #section : 나뉘어져야 하는 구간의 개수
    possible = True
    section = 1
    
    cnt = 0
    for i in range(N):
        #숫자 하나가 a보다 크면 구간을 나눌 수 없음
        if arr[i] > a:
            possible = False
            break

        #i번째 숫자가 들어갔을 때 a보다 커지면
        #i번째 숫자부터 다음 구간으로 만듬
        if cnt + arr[i] > a:
            cnt = 0
            section += 1
        
        #이번 구간에 i번째 숫자를 집어넣음
        cnt += arr[i]
    
    if possible and section <= M:
        ans = min(ans, a)
        break

print(ans)