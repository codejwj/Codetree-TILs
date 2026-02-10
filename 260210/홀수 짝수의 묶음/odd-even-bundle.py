N = int(input())
arr = list(map(int, input().split()))

even= 0
odd = 0
for elem in arr:
    if elem % 2 == 0:
        even += 1
    else:
        odd += 1

#만들어진 그룹의 총 개수
groups = 0
while True:
    #짝수 번째 그룹은 합이 '짝수'여야 함 
    if groups % 2 == 0:
        #짝수가 남아있다면 짝수 1개 사용 
        if even:
            even -= 1
            groups += 1
        #짝수가 없고 홀수가 2개 이상 있다면 홀수 2개 사용
        elif odd >= 2:
            odd -= 2
            groups += 1
        #짝수 그룹을 만들 수 없는 경우
        #남은 숫자가 있다면 마지막 그룹에 합쳐야 하므로
        #그룹 수 하나 감소
        else:
            if even > 0 or odd > 0:
                groups -= 1
            break

    #홀수 번째 그룹은 합이 '홀수'여야 함
    else:
        #홀수 숫자가 남아있다면 홀수 1개 사용 
        if odd:
            odd -= 1
            groups += 1
        #홀수가 하나도 없다면 더 이상 홀수 그룹 생성 불가
        else:
            break
    
print(groups)