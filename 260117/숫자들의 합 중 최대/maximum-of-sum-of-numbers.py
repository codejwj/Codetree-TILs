X, Y = tuple(map(int, input().split()))

#각 자리의 숫자의 합을 구하여 반환
def digit_sum(n):
    if n < 10:
        return n
    #두 자리 이상의 숫자라면, 맨 끝자리를 제외한 숫자들의 합을
    #재귀적으로 호출한 뒤, 그 결과가 마지막 자릿수를 더해 반환
    else:
        return digit_sum(n // 10) + (n % 10)

ans = 0
for i in range(X, Y + 1):
    ans = max(ans, digit_sum(i))
    
print(ans)