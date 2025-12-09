class Person:
    def __init__(self, name, h, w):
        self.name, self.h, self.w = name, h, w

arr = [tuple(input().split()) for _ in range(5)]
people = [Person(name, int(h), float(w)) for name, h, w in arr]

people.sort(key = lambda x: x.name)

print("name")
for person in people:
    print(person.name, person.h, person.w)
print()

people.sort(key = lambda x: -x.h)

print("height")
for person in people:
    print(person.name, person.h, person.w)