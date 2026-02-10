N = int(input())
arr = list(map(int, input().split()))

even_cnt = 0
odd_cnt = 0
for elem in arr:
    if elem % 2 == 0:
        even_cnt += 1
    elif elem % 2 != 0:
        odd_cnt += 1

ans = 0
target_is_even = True

while True:
    if target_is_even == True:
        if even_cnt > 0:
            even_cnt -= 1
            ans += 1
        elif even_cnt == 0 and odd_cnt >= 2:
            odd_cnt -= 2
            ans += 1
        else:
            break
    elif target_is_even == False:
        if odd_cnt > 0:
            odd_cnt -= 1
            ans += 1
        else:
            break
    
    target_is_even = not target_is_even

if odd_cnt == 1:
    ans -= 1

print(max(0, ans))