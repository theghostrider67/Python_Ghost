# Inheritance and Polymorphism

class Animal:
    location = "Italy"
    def __init__(self, name):
        self.name = name
    def speak(self):
    #    print("Generic animal sound")
       print("Speaking now......")
# a = Animal("Kutta")
# a.speak()

class Kutta(Animal):
    def speak(self):
        super().speak()
        print("Woof!")
    

d = Kutta("Jabir")
d.speak()
# print(d.location)