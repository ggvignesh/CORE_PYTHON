#5. Temperature — Static + Instance Method
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    def show_conversion(self):
        fahrenheit = Temperature.to_fahrenheit(self.celsius)
        print(f"Celsius = {self.celsius}")
        print(f"Fahrenheit = {fahrenheit}")

T1 = Temperature(25)
T2 = Temperature(100)

T1.show_conversion()
T2.show_conversion()