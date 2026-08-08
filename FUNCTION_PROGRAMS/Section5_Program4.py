#4. Write a function discount_price(price, discount=10) that returns the discounted price. Test with and without the discount argument.
def discount_price(price, discount=10):
    return price - (price * discount / 100)

print(discount_price(1000))
print(discount_price(1000, 20))