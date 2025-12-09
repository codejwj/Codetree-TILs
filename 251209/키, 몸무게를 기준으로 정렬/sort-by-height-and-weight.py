class Person:
    def __init__(self, name, h, w):
        self.name, self.h, self.w = name, h, w

n = int(input())
people = []
for _ in range(n):
    name, h, w = tuple(input().split())
    people.append(Person(name, int(h), int(w)))

people.sort(key = lambda x: (x.h, -x.w))

for person in people:
    print(person.name, person.h, person.w)