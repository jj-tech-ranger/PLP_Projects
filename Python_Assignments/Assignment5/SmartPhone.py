class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} is now OFF.")

    def make_call(self, number):
        if self.is_on:
            print(f"Calling {number} from {self.brand} {self.model}...")
        else:
            print("Please turn on the phone first.")

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Battery Life: {self.battery_life} hours")

my_phone = Smartphone("Apple", "iPhone 14", 20)
my_phone.display_info()
my_phone.turn_on()
my_phone.make_call("0712345678")
my_phone.turn_off()