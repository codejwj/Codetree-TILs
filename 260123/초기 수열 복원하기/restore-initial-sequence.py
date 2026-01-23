N = int(input())
arr = list(map(int, input().split()))

#첫 번째 숫자 a1을 1부터 N까지 하나씩 시도
for a1 in range(1, N + 1):
    #수열 A를 생성하고 첫 번째 숫자 추가 
    A = [a1]
    #현재 시도가 유효한지 추적하는 플래그 
    satisfied = True
    for i in range(N - 1):
        #합의 정의를 다음 숫자를 계산 
        a2 = arr[i] - A[i]

        #계산된 숫자가 1~N 범위를 벗어나거나 이미 수열에 존재하는지 확인
        if (a2 <= 0 or a2 > N) or (a2 in A):
            satisfied = False
            break
        
        #조건을 모두 만족하면 수열 A에 숫자 추가 
        A.append(a2)
    
    if satisfied:
        print(*A)
        break