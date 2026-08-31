#8. HotelRoom — Base Price + Bill Calculation
class HotelRoom:
    base_price = 3000

    def __init__(self, room_number, nights_booked, guest_name):
        self.room_number = room_number
        self.nights_booked = nights_booked
        self.guest_name = guest_name

    def total_bill(self):
        return self.nights_booked * HotelRoom.base_price

    @classmethod
    def update_base_price(cls, new_price):
        cls.base_price = new_price

    @staticmethod
    def valid_nights(nights):
        if type(nights) == int and nights > 0:
            return True
        else:
            return False

    def display(self):
        print(f"room_number = {self.room_number}")
        print(f"guest_name = {self.guest_name}")
        print(f"nights_booked = {self.nights_booked}")
        print(f"total_bill = {self.total_bill()}")

H1 = HotelRoom(101, 3, "Rajesh")
H2 = HotelRoom(102, 5, "Ramesh")

H1.display()
H2.display()

print("\nNight Validation:")

print("3 =", HotelRoom.valid_nights(3))
print("-2 =", HotelRoom.valid_nights(-2))
print("2.5 =", HotelRoom.valid_nights(2.5))

HotelRoom.update_base_price(4000)

print("\nAfter changing base price:")

H1.display()
H2.display()