class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [Person(name, int(height), int(weight)) for name, height, weight in arr]

people.sort(key = lambda x: x.height)

for person in people:
    print(person.name, person.height, person.weight)