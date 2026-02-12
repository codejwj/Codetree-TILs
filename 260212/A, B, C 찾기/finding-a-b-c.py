arr = list(map(int, input().split()))
#오름차순으로 정렬
arr.sort()

#가장 작은 숫자는 A, 두 번째로 작은 숫자는 항상 B
#가장 큰 숫자는 A + B + C 
#C는 끝 숫자 - A - B로 계산
A = arr[0]
B = arr[1]
C = arr[-1] - A - B

print(A, B, C)