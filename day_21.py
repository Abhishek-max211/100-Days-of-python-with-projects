# Day 21 
# Class Inheritance in Python
# Parent class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale... Exhale...")

# Child class
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water...")

# Create object of Fish
nemo = Fish()
nemo.breathe()   # Inherited from Animal
nemo.swim()      # Specific to Fish
print(f"Nemo has {nemo.num_eyes} eyes.")  # Inherited attribute

# Sample list
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Slicing examples
print(fruits[1:4])    # Output: ['Banana', 'Cherry', 'Date']
print(fruits[:3])     # Output: ['Apple', 'Banana', 'Cherry']
print(fruits[::2])    # Output: ['Apple', 'Cherry', 'Elderberry']
print(fruits[::-1])   # Output: ['Elderberry', 'Date', 'Cherry', 'Banana', 'Apple']
