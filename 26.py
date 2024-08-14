class Ticket:
    discount_rate = 0.28
    def __init__(self, movie_name, seat_number, price):
        self.mn = movie_name
        self.sn = seat_number
        self.price = price
        
    def details(self):
        print(self.mn, self.sn, self.price)
    
    def discount(self):
        print(self.price * Ticket.discount_rate)
        
        
m = Ticket('Titanic', '15', 1000)
m.details()