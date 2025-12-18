binary = input()
list(str(binary))
num = 0

for i in range(len(binary)):
    num = num * 2 + int(binary[i])

print(num)