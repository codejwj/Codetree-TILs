N = int(input())

def f(n):
    #1이면 더 이상 진행할 작업 없으므로 0회
    if n == 1:
        return 0
    
    #짝수라면 2로 나눠 진행했을 때의 횟수 + 1번 소요
    if n % 2 == 0:
        return f(n // 2) + 1
    #홀수라면 3으로 나눠 몫을 가지고 진행했을 때의 횟수 + 1번 소요
    else:
        return f(n // 3) + 1
    
print(f(N))