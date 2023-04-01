import ninja
class Pet:
    def __init__(self, name , type , tricks,sound ):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.sound=sound
        self.energy=0
        self.health=0
        
    def sleep(self):
        self.energy+=25
        return self
    def eat(self):
        self.energy+=5
        self.health+=10
        return self
    def play(self):
        self.health+=5
        return self
    def noise(self):
        print(self.sound)
        return self

dog=Pet("tom","german shepherd","nothing special","barking")

souheil=ninja.Ninja("souheil","khalfallah",dog)
souheil.feed().walk().bathe()

print(souheil.pet.energy)
print(souheil.pet.health)