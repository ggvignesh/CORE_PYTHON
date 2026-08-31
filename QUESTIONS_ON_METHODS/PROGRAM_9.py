#9. delivery service
class Delivery_Service:
    @staticmethod
    def delivery_charge(amount):
        if amount >= 500:
            return 0
        return 108
print(Delivery_Service.delivery_charge(400))