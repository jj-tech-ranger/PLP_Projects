class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

def vehicle_movement(vehicle):
    vehicle.move()

car = Car()
plane = Plane()
bicycle = Bicycle()

vehicle_movement(car)
vehicle_movement(plane)
vehicle_movement(bicycle)