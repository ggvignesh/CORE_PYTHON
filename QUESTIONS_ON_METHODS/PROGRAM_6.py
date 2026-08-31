#6. change_hospital(new_name) to update hospital name
class Hospital:
    hospital_name = "City Hospital"
    def __init__(self,name,address):
        self.name = name
        self.address = address
    def display(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
    @classmethod
    def change_hospital(cls,new_name):
        cls.hospital_name = new_name
H1 = Hospital("National Hospital","Hyderabad")
H2 = Hospital("Anupama Hospital","Chennai")
H3 = Hospital("Visakha Eye Hospital","Vizag")
H1.display()
H1.change_hospital(new_name="Life Care Hospital")
H1.display()