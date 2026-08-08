#9. Write a function shopping_cart(item_name).
# The outer function receives the item name.
# The inner function receives:
    #quantity
    #price per item
# Print the item name, quantity, and total price.
# Return the inner function.
def shopping_cart(item_name):
    def cart(quantity, price_per_item):
        total = quantity * price_per_item
        print("Item:", item_name)
        print("Quantity:", quantity)
        print("Total Price =", total)
    return cart

c = shopping_cart("Laptop")
c(2, 45000)