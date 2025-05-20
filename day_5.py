# Day 5
# Using the For Loop with Python Lists
Fruits=["Apples","Banana","Pear","Grapes"]
for fruit in Fruits:
    print(fruit)
    print(fruit+" pie")

print(Fruits)

# Highest Number in the list
Numbers=[10,20,34,56,78,54,98,66,76,64,33,46,55]
num=0
for item in Numbers:
    if item>num:
       num=item
print(num)

# Sum of the Numbers in the list
Numbers=[10,20,34,56,78,54,98,66,76,64,33,46,55]
sum=0
for item in Numbers:
    sum+=item
print(sum)

# For Loop with Range Function
num=int(input("Enter the Number:"))
for item in range(1,num+1):
    print(item,end=" ")
print("\n")
for item in range(1,num+1,2):# range(initial,final,step-size)
    print(item,end=" ")

# Sum of Numbers from 1 to 100
sum=0
for num in range(1,101):
    sum+=num
print(f"\nThe Sum of from 1 to 100 is {sum}")
print("Thank You for visiting!")