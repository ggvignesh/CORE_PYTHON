#8. return the ticket price(movie) based on age
class Movie_Ticket:
    def __init__(self,movie_name,ticket_price):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
    def display(self):
        print(f"movie_name = {self.movie_name}")
        print(f"ticket_price = {self.ticket_price}")
    @staticmethod
    def ticket_price(age):
        if age<12:
            return 100
        elif age>=12 and age<=60:
            return 200
        else:
            return 150
print(Movie_Ticket.ticket_price(20))