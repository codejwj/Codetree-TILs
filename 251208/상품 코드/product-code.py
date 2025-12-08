class Product:
    def __init__(self, name = "codetree", code = 50):
        self.name = name
        self.code = code

p1 = Product()
print(f"product {p1.code} is {p1.name}")

name, code = input().split()
code = int(code)

p2 = Product(name, code)
print(f"product {p2.code} is {p2.name}")