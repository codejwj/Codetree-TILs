class Sequence:
    def __init__(self, elem, idx):
        self.elem, self.idx = elem, idx

n = int(input())
arr = list(map(int, input().split()))

sequences = []
sequences = [Sequence(elem, i) for i, elem in enumerate(arr)]
result = [0 for _ in range(n)]

#Custom Comparator를 활용한 정렬
sequences.sort(key = lambda x: (x.elem, x.idx))

#정렬된 숫자들의 원래 인덱스를 활용한 결과 배열 저장
for i, elem in enumerate(sequences):
    result[elem.idx] = i + 1 #인덱스 보정

for i in range(n):
    print(result[i], end = " ")