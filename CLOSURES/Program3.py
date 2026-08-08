#3. Write a function discount(percent).
# The outer function receives the discount percentage.
# The inner function receives the product price.
# Print the final price after applying the discount.
# Return the inner function.
def discount(percent):
    def final_price(price):
        amount = price - (price * percent / 100)
        print("Final Price =", amount)
    return final_price

d = discount(20)
d(1000)