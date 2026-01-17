X, Y = tuple(map(int, input().split()))

cnt = 0
for i in range(X, Y + 1):
    str_i = str(i)
    #펠린드롬 수는 거꾸로 읽어도 똑같은 수
    if str_i == str_i[::-1]:
        cnt += 1

print(cnt)