n = int(input())
word = [input() for _ in range(n)]

word.sort()
for elem in word:
    print(elem)