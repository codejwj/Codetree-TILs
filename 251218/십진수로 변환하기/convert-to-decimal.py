binary = list(map(int, list(input())))
num = 0

for i in range(len(binary)):
    num = num * 2 + binary[i]

print(num)