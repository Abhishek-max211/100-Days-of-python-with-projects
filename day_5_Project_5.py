# Project-5 = Python Password Generator
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!',"@","#","$","&","*"]

print("Welcome to Python Password Generator!")
user_letters=int(input("How many letters would you like in your Password? "))
user_numbers=int(input("How many numbers would you like in your Password? "))
user_symbols=int(input("How many symbols would you like in your Password? "))

password_list=[]
for char in range(1,user_letters+1):
    password_list.append(random.choice(letters))

for char in range(1,user_numbers+1):
    password_list.append(random.choice(numbers))

for char in range(1,user_symbols+1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)

password=""
for char in password_list:
    password+=char
print(f"\nYou Generated Password is= {password}\n")