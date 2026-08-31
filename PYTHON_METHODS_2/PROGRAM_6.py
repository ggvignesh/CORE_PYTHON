#6. Vehicle — Service Rate + Service History
class Vehicle:
    service_rate = 5

    def __init__(self, model, kilometers_run, service_history):
        self.model = model
        self.kilometers_run = kilometers_run
        self.service_history = service_history

    def service_charge(self):
        return self.kilometers_run * Vehicle.service_rate

    @classmethod
    def update_service_rate(cls, new_rate):
        cls.service_rate = new_rate

    @staticmethod
    def service_eligible(year):
        current_year = 2026

        if current_year - year <= 15:
            return True
        else:
            return False

    def display(self):
        print(f"model = {self.model}")
        print(f"kilometers_run = {self.kilometers_run}")
        print(f"service_history = {self.service_history}")
        print(f"service_charge = {self.service_charge()}")

V1 = Vehicle("Toyota", 20000, "Regular Service")
V2 = Vehicle("Honda", 30000, "Oil Change")
V3 = Vehicle("Ford", 50000, "Major Service")

V1.display()
V2.display()
V3.display()

print("\nService Eligibility:")

print("Toyota 2020 =", Vehicle.service_eligible(2020))
print("Ford 2005 =", Vehicle.service_eligible(2005))

Vehicle.update_service_rate(8)

print("\nAfter updating service rate:")

V1.display()
V2.display()
V3.display()