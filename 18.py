class Team:
    def __init__(self, name):
        self.name = name
        self.members = []
        
    def add_member(self):
        self.members.append(self.name)
        print('member added successfully..')
        print(self.members)
    def remove_member(self):
        self.members.remove(self.name)
        print('member removed successfully..')
        print(self.members)
        
        
hamid = Team('Hamid')
hamid.add_member()

homayon = Team('Homayoun')
homayon.add_member()
homayon.remove_member()