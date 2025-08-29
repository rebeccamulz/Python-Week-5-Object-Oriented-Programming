"""
OOP Assignment 🚀
Assignment 1: Design Your Own Class
Assignment 2: Polymorphism Challenge
"""

# ------------------------------
# Assignment 1: Design Your Own Class
# ------------------------------

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")
    
    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")

# Inherited class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        # Call parent constructor
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system
    
    # Extra method
    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} with {self.cooling_system} cooling 🎮")

# ------------------------------
# Assignment 2: Polymorphism Challenge
# ------------------------------

class Animal:
    def move(self):
        print("Animals can move in different ways...")

class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🕊️")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

# ------------------------------
# Test Code
# ------------------------------

# Assignment 1 Test
print("=== Smartphone Classes ===")
phone1 = Smartphone("Samsung", "Galaxy S24", 256)
phone1.info()
phone1.call("123456789")

gaming_phone = GamingPhone("Asus", "ROG Phone 7", 512, "liquid-cooling")
gaming_phone.info()
gaming_phone.play_game("PUBG")

# Assignment 2 Test
print("\n=== Polymorphism with Animals ===")
animals = [Dog(), Bird(), Fish()]
for a in animals:
    a.move()
