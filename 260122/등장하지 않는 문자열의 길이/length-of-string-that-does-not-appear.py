N = int(input())
s = input()

#찾으려는 부분의 문자열의 길이의 범위
for i in range(1, N + 1):
    #현재 검사 중인 길이 i가 정답이 될 수 있는가?
    flag = True
    for j in range(N - i + 1):
        sub_s = s[j : j + i]
        #중복 체크
        #현재 뽑아낸 부분 문자열이 그 뒤의 남은 문자열에 또 존재하는지 확인
        if sub_s in s[j + 1 : ]:
            flag = False
            break
    
    #길이 i인 모든 부분 문자열이 중복되지 않으므로 최소 길이 i 출력
    if flag:
        print(i)
        break