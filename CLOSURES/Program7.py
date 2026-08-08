#7. Write a function restaurant(food_item).
# The outer function stores the food item.
# The inner function receives the quantity.
# Print the order details.
# Return the inner function.
def restaurant(food_item):
    def order(quantity):
        print("Food Item:", food_item)
        print("Quantity:", quantity)
    return order

r = restaurant("Pizza")
r(3)