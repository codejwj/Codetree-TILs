class Product:
    def __init__(self, product_name = "codetree", product_code = 50):
        self.product_name = product_name
        self.product_code = product_code

p1 = Product()
print(f"product {p1.product_code} is {p1.product_name}")

product_name, product_code = input().split()
product_code = int(product_code)

p2 = Product(product_name, product_code)
print(f"product {p2.product_code} is {p2.product_name}")