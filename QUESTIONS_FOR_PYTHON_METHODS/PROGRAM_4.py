#4. Car — Instance + Class Method
class Car:
    wheels = 4

    def __init__(self, mileage):
        self.mileage = mileage

    def display_specs(self):
        print(f"mileage = {self.mileage}")
        print(f"wheels = {self.wheels}")

    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels

C1 = Car(20)
C2 = Car(25)

C1.display_specs()
C2.display_specs()

Car.change_wheels(6)

print("\nAfter changing wheels:")

C1.display_specs()
C2.display_specs()