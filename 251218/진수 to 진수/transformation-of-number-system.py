A, B = map(int, input().split())
N = list(map(int, list(input())))
num = 0

for i in range(len(N)):
    num = num * A + N[i]

digits = []

while True:
    if num < B:
        digits.append(num)
        break
    
    digits.append(num % B)
    num //= B 

for digit in digits:
    print(digit, end = "")