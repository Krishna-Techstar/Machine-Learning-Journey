from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def Make_sound(self):
        pass

class Lion(Animal):
    def Make_sound(self):
        print("Roar!")

class Cow(Animal):
    def Make_sound(self):
        print("Meow!")

Lion =Lion()
Lion.Make_sound()

Cow = Cow()
Cow.Make_sound()
        