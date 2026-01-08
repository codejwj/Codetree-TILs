import sys

INT_MIN = -sys.maxsize

a = list(map(int, list(input())))

#각 i번째 자릿수를 바꾸었을 때의 십진수 값을 구함
max_val = INT_MIN
for i in range(len(a)):
    #i번째 자릿수를 바꿈
    a[i] = 1 - a[i]

    #십진수로 변환
    num = 0
    for j in range(len(a)):
        num = num * 2 + a[j]
        
    max_val = max(max_val, num)
    #i번째 자릿수를 원래대로 돌려놓음
    a[i] = 1 - a[i]

print(max_val)