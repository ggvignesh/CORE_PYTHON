#4. Rewrite this call using keyword arguments: book_ticket('Alice', 'Delhi', 'Mumbai', 2)
def book_ticket(name, source, destination, tickets):
    print("Name        :", name)
    print("Source      :", source)
    print("Destination :", destination)
    print("Tickets     :", tickets)

book_ticket(
    destination="Mumbai",
    tickets=2,
    name="Alice",
    source="Delhi"
)