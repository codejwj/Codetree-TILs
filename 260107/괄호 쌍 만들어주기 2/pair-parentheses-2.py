A = input()
N = len(A)

cnt = 0
for i in range(N):
    for j in range(i + 2, N - 1):
        if A[i] == '(' and A[i + 1] == '(':
            if A[j] == ')' and A[j + 1] == ')':
                cnt += 1
        
print(cnt)