N, B = map(int, input().split())
digits1 = []
digits2 = []

if B == 4:
    while True:
        if N < 4:
            digits1.append(N)
            break
        
        digits1.append(N % 4)
        N //= 4
    
    for digit in digits1[::-1]:
        print(digit, end = "")

if B == 8:
    while True:
        if N < 8:
            digits2.append(N)
            break
        
        digits2.append(N % 8)
        N //= 8

    for digit in digits2[::-1]:
        print(digit, end = "")