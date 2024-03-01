from abc import abstractmethod


class Animal:

    def __init__(self, name, color, id):
        self.name = name
        self.color = color
        self.id = id

    def make_sound(self):
        print("I'm making a sound!!!!")

    def run(self):
        print("Look! I'm running really fast!")


class Bird(Animal):

    def __init__(self, name, color, id, location):
        self.location = location
        Animal.__init__(self, name, color, id)

    def make_sound(self):
        print("TWEET tweet tweet! I said, tweet!")

    def run(self):
        print("I'm actually flying!")

class Cat(Animal):

    def make_sound(self):
        print("Meow! Meoooow!")


class Dog():
    @abstractmethod
    def fetch(self):
        pass

class Spike(Dog):

    def fetch(self):
        print("Spike likes to fetch sticks")


kitty = Animal("Super Kitty", "dark", 313123)
# print(kitty.color)
# print(kitty.name)
kitty.make_sound()

kitty_2 = Cat("Another Kitty", "white", 9997)
kitty_2.make_sound()

tweety = Bird("Super Tweety", "yellow", 5395893, "USA")
# print(tweety.color)
# print(tweety.location)
tweety.make_sound()
# tweety.run()
tweety.run()

spike = Spike()
spike.fetch()