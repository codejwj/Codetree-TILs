N, K, T = input().split()
N, K = int(N), int(K)
word = [input() for _ in range(N)]

T_len = len(T)
new_word = []

word.sort()
for elem in word:
    if elem[0 : T_len] == T:
        new_word.append(elem)

for i in range(len(new_word)):
    if i == K - 1:
        print(new_word[i])