#2. Product — Class Tax Rate + Instance Method + Class Method + Static Method
class Product:
    tax_rate = 0.10

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def final_price(self):
        return self.base_price + (self.base_price * Product.tax_rate)

    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

    @staticmethod
    def is_valid_price(price):
        if price >= 0 and price <= 1000000:
            return True
        else:
            return False

    def display(self):
        print(f"name = {self.name}")
        print(f"base_price = {self.base_price}")
        print(f"final_price = {self.final_price()}")

P1 = Product("Laptop", 50000)
P2 = Product("Mobile", 30000)
P3 = Product("Tablet", 20000)

P1.display()
P2.display()
P3.display()

print("\nPrice Validation:")

print("50000 =", Product.is_valid_price(50000))
print("-100 =", Product.is_valid_price(-100))

Product.change_tax_rate(0.20)

print("\nAfter changing tax rate:")

P1.display()
P2.display()
P3.display()