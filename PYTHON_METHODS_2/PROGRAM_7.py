#7. Inventory — Stock Dictionary + Global Threshold
class Inventory:
    total_items = 0
    minimum_stock = 5

    def __init__(self, stock):
        self.stock = stock
        Inventory.total_items = Inventory.total_items + sum(stock.values())

    def add_stock(self, item, quantity):
        if item in self.stock:
            self.stock[item] = self.stock[item] + quantity
        else:
            self.stock[item] = quantity

        Inventory.total_items = Inventory.total_items + quantity

    def remove_stock(self, item, quantity):
        if item in self.stock and self.stock[item] >= quantity:
            self.stock[item] = self.stock[item] - quantity
            Inventory.total_items = Inventory.total_items - quantity
            print(quantity, item, "removed")
        else:
            print("Insufficient stock")

    @classmethod
    def update_threshold(cls, new_threshold):
        cls.minimum_stock = new_threshold

    @staticmethod
    def below_threshold(quantity):
        if quantity < Inventory.minimum_stock:
            return True
        else:
            return False

    def display(self):
        print(self.stock)

I1 = Inventory({"Laptop": 10, "Mouse": 20})
I2 = Inventory({"Keyboard": 8, "Monitor": 6})

print("Inventory 1:")
I1.display()

print("Inventory 2:")
I2.display()

I1.add_stock("Laptop", 5)
I2.remove_stock("Keyboard", 3)

print("\nAfter stock changes:")

I1.display()
I2.display()

Inventory.update_threshold(10)

print("\nMinimum stock threshold =", Inventory.minimum_stock)

print("Laptop stock below threshold:",
      Inventory.below_threshold(I1.stock["Laptop"]))

print("Keyboard stock below threshold:",
      Inventory.below_threshold(I2.stock["Keyboard"]))

print("\nTotal items =", Inventory.total_items)