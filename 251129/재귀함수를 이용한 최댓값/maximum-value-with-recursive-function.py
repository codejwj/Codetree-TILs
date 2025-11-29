n = int(input())
arr = list(map(int, input().split()))

#a번째까지 인덱스의 숫자 중에 가장 큰 값을 반환
def max_value(a):
    if a == 0:
        return arr[0]
    
    return max(max_value(a - 1), arr[a])

print(max_value(n - 1))