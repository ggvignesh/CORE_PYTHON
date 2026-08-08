#5. Write a function movie(movie_name).
# The outer function stores the movie name.
# The inner function receives the person’s name.
# Print that the person booked a ticket for the movie.
# Return the inner function.
def movie(movie_name):
    def booking(person_name):
        print(person_name, "booked a ticket for", movie_name)
    return booking

m = movie("Pushpa 2")
m("Vignesh")