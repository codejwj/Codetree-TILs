class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
p = [Person(name, int(height), int(weight)) for name, height, weight in arr]

p.sort(key = lambda x: x.height)

for person in p:
    print(person.name, person.height, person.weight)