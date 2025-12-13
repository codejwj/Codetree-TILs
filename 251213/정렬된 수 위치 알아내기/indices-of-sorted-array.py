class Sequence:
    def __init__(self, elem, num):
        self.elem, self.num = elem, num

n = int(input())
elem = list(map(int, input().split()))

sequences = []
for i in range(len(elem)):
    sequences.append(Sequence(elem[i], i))

sequences.sort(key = lambda x: (x.elem, x.num))

result = [0] * n
for new_idx in range(n):
    sequence = sequences[new_idx]
    old_idx = sequence.num
    result[old_idx] = new_idx

for idx in result:
    print(idx + 1, end = " ")