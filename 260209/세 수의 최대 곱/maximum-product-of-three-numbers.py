N = int(input())
arr = list(map(int, input().split()))

#case 1. 양의 정수 3개
#case 2. 양의 정수 2개, 음의 정수 1개
#case 3. 양의 정수 1개, 음의 정수 2개
#case 4. 음의 정수 3개
#case 5. 0을 포함하여 선택

arr.sort()
#case 1에 해당
num1 = arr[-1] * arr[-2] * arr[-3]
#case 3에 해당
num2 = arr[0] * arr[1] * arr[-1]
print(max(num1, num2))