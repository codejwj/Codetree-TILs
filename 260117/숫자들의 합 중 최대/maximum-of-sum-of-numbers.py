X, Y = tuple(map(int, input().split()))

ans = 0
for num in range(X, Y + 1):
    str_num = str(num)
    char_num = list(str_num)
    int_num = list(map(int, char_num))
    sum_val = sum(int_num)

    ans = max(ans, sum_val)
    
print(ans)