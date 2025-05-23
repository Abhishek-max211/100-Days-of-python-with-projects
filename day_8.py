# Day 8
# Function with Inputs in Python
def greet(name):
    print(f"Hello {name}")
    print(f"Welcome {name}")
    print(f"Have a Good Day {name}")
# Call the Function
greet("Abhishek")

# Positional Arguments in python
def greet(name,location):
    print(f"\nWelcome {name}")
    print(f"I live in {location}")
greet("Uttar Pradesh","Abhishek")

# Keyword Arguments
def greet(name,location):
    print(f"\nWelcome {name}")
    print(f"I live in {location}")
greet(location="Uttar Pradesh",name="Abhishek")

# Function of sum Two Numbers
num1=float(input("\nEnter The First Number:"))
num2=float(input("Enter the Second Number:"))
def sum(a,b):
    sum=a+b
    print(f"The sum of two numbers is {sum}\n")
sum(a=num1,b=num2)

print("Thank you for visiting!")