class Ninja:

    def __init__(self, first_name , last_name,pet ):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=""
        self.pet_food=0
        self.pet= pet
    
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):                            
        self.pet.noise()
        return self