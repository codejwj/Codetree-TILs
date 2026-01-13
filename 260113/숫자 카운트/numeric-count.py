N = int(input())
arr = []

for _ in range(N):
    num, cnt1, cnt2 = tuple(map(int, input().split()))
    arr.append((num, cnt1, cnt2))

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            
            check = True

            for n, s, b in arr:
                n1 = n // 100
                n2 = (n // 10) % 10
                n3 = n % 10

                cnt_s = 0
                cnt_b = 0

                if i == n1: cnt_s += 1
                if j == n2: cnt_s += 1
                if k == n3: cnt_s += 1
                    
                if i == n2 or i == n3: cnt_b += 1
                if j == n1 or j == n3: cnt_b += 1
                if k == n1 or k == n2: cnt_b += 1

                if cnt_s != s or cnt_b != b:
                    check = False
                    break
            
            if check:
                cnt += 1

print(cnt)