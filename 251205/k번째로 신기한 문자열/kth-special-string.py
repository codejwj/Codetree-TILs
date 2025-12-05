N, K, T = input().split()
N, K = int(N), int(K)
word = [input() for _ in range(N)]

T_len = len(T)
result = []

word.sort()
for elem in word:
    if elem[0 : T_len] == T:
        result.append(elem)

print(result[K - 1])