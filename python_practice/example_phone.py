class Phone():

    # Initializer
    def __init__(self, color, make, model, num_of_cameras, memory="512GB"):
        self.color = color
        self.make = make
        self.model = model
        self.num_of_cameras = num_of_cameras
        self.memory = memory

    def make_call(self):
        print("Wow! I'm making a call!")


    def send_text_message(self):
        print("I'm sending a message")


rodislavas_iphone = Phone('purple', 'Apple', 'iPhone 13 Pro', 3, memory="1TB")
print(rodislavas_iphone.color)
print(rodislavas_iphone.model)
rodislavas_iphone.make_call()
print((rodislavas_iphone.memory))

yuryis_iphone = Phone("silver", "Apple", "iPhone 14 Pro Max", 3)
print(yuryis_iphone.color)

# kates_iphone = Phone()
# print(kates_iphone.color)
# print(kates_iphone.model)
# kates_iphone.make_call()