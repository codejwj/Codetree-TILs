class Home:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

homes = []

n = int(input())
for _ in range(n):
    name, addr, city = tuple(input().split())
    homes.append(Home(name, addr, city))

idx = 0
for i in range(n):
    if homes[idx].name < homes[i].name:
        idx = i

print(f"name {homes[idx].name}")
print(f"addr {homes[idx].addr}")
print(f"city {homes[idx].city}")