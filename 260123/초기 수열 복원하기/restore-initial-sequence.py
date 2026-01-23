N = int(input())
arr = list(map(int, input().split()))

for a1 in range(1, N + 1):
    A = []
    A.append(a1)
    possible = True
    for i in range(N - 1):
        a2 = arr[i] - A[i]

        if (a2 < 1 or a2 > N) or (a2 in A):
            possible = False
            break
        
        A.append(a2)
    
    if possible:
        print(*A)
        break