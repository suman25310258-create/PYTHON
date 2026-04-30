class Dog:
    def sound(self):
        print("Dog says: Woof!")
        
class Cat:
    def sound(self):
        print("Cat says Meow!")
        

def make_sound(animal):
    animal.sound()
    

d=Dog()
c=Cat()

make_sound(d)
make_sound(c)
