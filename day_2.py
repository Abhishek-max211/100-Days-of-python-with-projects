# Day 2
# Primitive datatypes in python

# 1.String
# len() function
user_input=input("Enter Your Name? ")
print("The length of your name is=",len(user_input))
# In Python type() function is used to identify the type of the datatype
print("the Type oF the value",type(user_input))
# String Subscripting 
print("Hello"[0]) # Here 0 is the index Number
print("Hello"[1]) # Here 1 is the index Number
print("Hello"[2]) # Here 2 is the index Number
print("Hello"[3]) # Here 3 is the index Number
print("Hello"[4]) # Here 4 is the index Number

# 2. Integer
a=3456
print(123+345) # Integer = Whole Number
# large Integer
print(123_233_444)
print("the Type of the value",type(a))
# In Python type() function is used to identify the type of the datatype

# 3. Float 
b=567.99
print(b)
print("The type is ",type(b))
# In Python type() function is used to identify the type of the datatype

# 4. Boolean
d=(True or False)
print(d)
print("The type is ",type(d))
# In Python type() function is used to identify the type of the datatype

# Type Conversion
p=("123"+"223")
print(p)
print(type(p))
n=int("123")+int("223")
print(n)
print(type(n))
e=(123+34.5)
print(e)
print(type(e))
print("Number of letters in your name"+" "+str(len(input("What is your nmae? "))))
# In python predefined functions are used for type conversion

# Mathematical operations 
# Basic operators are= +,-,/,*,//,**
print(23+45)
print(2334-445)
print(36/6)
print(34*3)
print(36//6)
print(2**3)
 
# Number Manipulation
# Float to int coversion
a=2344.556
print(a)
print(int(a))
# Rounding a number
a=3.3
b=3.9
c=232.44555666
print(round(a))
print(round(b))
print(round(c,2))

# f-string in python
name="Ahishek"
Age=12
marks=82.65
print(f"My name is{name}")
print(f"I am {Age} years old")
print(f"{marks} is my marks")
print("Thank You for visiting")
