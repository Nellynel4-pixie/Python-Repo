# Activity 1 
#Base Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Derived Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)  # Call base constructor
        self.gpu = gpu

    # Polymorphism: overriding info()
    def info(self):
        print(f"{self.brand} {self.model} [Gaming Edition]")
        print(f"Storage: {self.storage}GB, GPU: {self.gpu}")

    def play_game(self, game):
        print(f"Playing {game} smoothly with {self.gpu} GPU!")

# Create Objects
phone1 = Smartphone("Samsung", "S24", 256)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, "Adreno 740")

# Test Methods
phone1.info()
phone1.call("123-456-789")

print("---")

phone2.info()
phone2.call("987-654-321")
phone2.play_game("Genshin Impact")

# Activity 2: Polymorphism Challenge
print("\n=== Vehicle Polymorphism Demo ===")

class Vehicle:
    def move(self):
        pass  # placeholder for polymorphism

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat()]

# Loop through and call move()
for v in vehicles:
    v.move()