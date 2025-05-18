# Day 3
# Comparsion Operators in python are >,<,>=,<=,==,!= and modulo operator %
# Logical Operator in python are and,or,not
# Conditional Statements
# 1. if-else statement
print("if-else statement")
number=int(input("Enter the number:"))
if number%2==0:
    print(f"{number} is even\n")
else:    
    print(f"{number} is odd\n")

# 2. Nested if-else statement
print("Nested if-else statement")
print("Welcome to the rollercoatler!")
height=int(input("What is your height in cm? "))
if height>=120:
    print("You can ride the rollercoastler!")
    age=int(input("What's your Age? "))
    if age <=18:
        print("Please Pay $7\n")
    else:
        print("Please Pay $12\n")    
else:
    print("Sorry You can not ride the rollercoastler!\n")

# 3. if-elif-else statement
print("if-elif-else statement")
print("Welcome to the rollercoastler!")
height=int(input("What is your height in cm? "))
if height>=120:
    print("You can ride the rollercoastler!")
    age=int(input("What's your Age? "))
    if age <=12:
        print("Please Pay $5\n")
    elif age <=18:
        print("Please Pay $7\n")
    else:
        print("Please Pay $12\n")    
else:
    print("Sorry You can not ride the rollercoastler!\n")

# 4. Multiple if-statement in succession
print("if-elif-else statement")
print("Welcome to the rollercoastler!")
height=int(input("What is your height in cm? "))
bill=0
if height>=120:
    print("You can ride the rollercoastler!")
    age=int(input("What's your Age? "))
    if age <=12:
        print("Child tickets are $5\n")
        bill=5
    elif age <=18:
        print("Youth tickets are $7\n")
        bil=7
    else:
        print("Adult tickets are $12\n") 
        bill=12

        wants_photos=input("Do you want a picture take for $3? type y for yes and n for no ").lower()
        if wants_photos=="y":
            bill += 3
            print(f"Your total bill is {bill}")
            print("Thank you for visiting!")
        else:
            print(f"Your total bill is {bill}")
            print("Thank you for visiting!")    
else:
    print("Sorry You can not ride the rollercoastler!\n")
