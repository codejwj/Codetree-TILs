N = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

cnt = 0
#백의 자리 수 i, 십의 자리 수 j, 일의 자리 수  k
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            
            checked = True

            for num, num_cnt1, num_cnt2 in arr:
                #n1:백의 자리 수, n2:십의 자리 수, n3:일의 자리 수
                n1 = num // 100
                n2 = (num // 10) % 10
                n3 = num % 10

                #1번 카운트, 2번 카운트
                cnt1 = 0
                cnt2 = 0

                if n1 == i: cnt1 += 1
                if n2 == j: cnt1 += 1
                if n3 == k: cnt1 += 1
                    
                if n1 == j or n1 == k: cnt2 += 1
                if n2 == i or n2 == k: cnt2 += 1
                if n3 == i or n3 == j: cnt2 += 1

                #카운트 수가 다르면 정답 아님
                if cnt1 != num_cnt1 or cnt2 != num_cnt2:
                    checked = False
                    break
            
            if checked:
                cnt += 1

print(cnt)