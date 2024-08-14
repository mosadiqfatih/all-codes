class Room:
    def __init__(self, room_number: int, is_occupied: bool):
        self.room_no = room_number
        self.is_occupied = is_occupied
            
room1 = Room(1, True)
room2 = Room(2, False)
room3 = Room(3, False)
room4 = Room(4, False)
room5 = Room(5, True)
room6 = Room(6, False)
room7 = Room(7, True)
room8 = Room(8, True)
room9 = Room(9, False)
room10 = Room(10, False)

  
class Hotel:
    def __init__(self, name):
        self.name = name
        self.room = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10]
        
    def check(self, room_no: int):
        if self.room[room_no-1].is_occupied == True:
            print('Room is occupied..')
        else:
            print('Room is Free..')
                
    def book(self, room_no: int):
        if self.room[room_no-1].is_occupied == True:
            print('It is already booked..')
        else:
            self.room[room_no-1].is_occupied = True
            print('You are Welcome, My Lord!')
                

h1 = Hotel('Abas&Mahgol Ltd')
# h1.check(0)

# h1.book(0)
# h1.book(1)
h1.check(10)