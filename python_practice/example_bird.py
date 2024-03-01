class Bird:

    def __init__(self, color, name):
        self.color = color
        self.name = name

    #field 
    age = 100

    def make_sound(self):
        print("Tweet tweet tweet!")

    def fly(self):
        print("Hey! I'm flying!")



tweety = Bird("yellow", "Tweety")
print(tweety.color)
print(tweety.name)
tweety.make_sound()
tweety.fly()
print(tweety.age)

brother_of_tweety = Bird("orange", "Brother of Tweety")
print(brother_of_tweety.color)
print(brother_of_tweety.name)
brother_of_tweety.make_sound()
brother_of_tweety.fly()
print(brother_of_tweety.age)