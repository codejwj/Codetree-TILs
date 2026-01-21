N = int(input())
s = input()

for i in range(1, N + 1):
    found = True
    for j in range(N - i + 1):
        sub_s = s[j : i + j]
        if sub_s in s[j + 1 : ]:
            found = False
            break
        
    if found:
        print(i)
        break