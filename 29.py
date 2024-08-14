class Flight:
    def __init__(self, flight_number, destination, passengers=None):
        self.fn = flight_number
        self.destination = destination
        if passengers == None:
            self.passengers = []
        else:
            self.passengers = passengers
            
    def add_passengers(self, person):
        self.passengers.append(person)
        
        
    def remove_passengers(self, person):
        self.passengers.remove(person)
        
    def pass_list(self):
        return self.passengers
    
    
f1 = Flight(12, 'Moscow', ['Parisa', 'Banoo', 'Sodaba The Cousin', 'Abas', 'Zaman', 'Zaki Sarcheshmayi'])
f1.add_passengers('Sadiq')
f1.add_passengers('S****')
print(f1.pass_list())