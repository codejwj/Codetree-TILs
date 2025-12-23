N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

infected = [False] * (N + 1)
infected[P] = True

counts = [0] * (N + 1)
counts[P] = K

handshakes.sort()
for t, x, y in handshakes:
    x_infected = infected[x]
    y_infected = infected[y]

    if x_infected and counts[x] > 0:
        if not y_infected:
            infected[y] = True
            counts[y] = K
        counts[x] -= 1
    
    if y_infected and counts[y] > 0:
        if not x_infected:
            infected[x] = True
            counts[x] = K
        counts[y] -= 1

for i in range(1, N + 1):
    if infected[i] == True:
        print(1, end = "")
    else:
        print(0, end = "")