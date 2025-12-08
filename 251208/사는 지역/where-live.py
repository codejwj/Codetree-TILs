class Address:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

people = []

n = int(input())
for _ in range(n):
    name, addr, city = tuple(input().split())
    people.append(Address(name, addr, city))

#사전순으로 이름이 가장 느린 사람 찾기
idx = 0
for i in range(n):
    if people[idx].name < people[i].name:
        idx = i

print(f"name {people[idx].name}")
print(f"addr {people[idx].addr}")
print(f"city {people[idx].city}")