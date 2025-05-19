# Day 4
# Randomisation in python
# Use of random module
import random
# For integers
random_input=random.randint(1,10)
print(f"Show differnt number={random_input} ")

# For Floating Numbers
user=random.random()
print(user)
# Or we can use this also
random_float=random.uniform(1,10)
print(random_float)

# Program that prints Heads and Tails at random
choice=random.randint(0,1)
if choice==0:
    print("Heads")
else:
    print("Tails")

# Lists in python
List_of_Names=["Abhi","Rohan","Sanjay","Rahul"]
print(List_of_Names)
print(List_of_Names[0]) # index number of the element
print(List_of_Names[1])
print(List_of_Names[2])
print(List_of_Names[3])
# How to Change the variable
List_of_Names[2]="Sudhanshu"
print(List_of_Names)
# random choice function
names=random.choice(List_of_Names)
print(f"{names} will pay the bill.")

# Nested Lists in python
fruits=["Strawberries","Nectaries","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables=["Spinach","Kale","Tomatoes","Cherry","Potatos"]
dirty_dozen=[fruits,vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

numbers=[10,9,[13,45,67,29],56,7,5]
print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
print(numbers[2][0])
print(numbers[2][1])
print(numbers[2][2])
print(numbers[2][3])
print("Thank you for Visting!")