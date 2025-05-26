# Day 10
# Functions with outputs

def my_function():
    result = 3 * 2
    return result  # result is the output

output = my_function()
print(output)


# Example with names
def format_name(fname, lname):
    print(fname.title())
    print(lname.title())

format_name("abhisheK", "ABHISHEK")


# Function with return values
def format_name(fname, lname):
    formatted_fname = fname.title()
    formatted_lname = lname.title()
    return f"{formatted_fname} {formatted_lname}"

output = format_name("AbhisheK", "Pundir")
print(output)


# Function chaining
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)


# Multiple return values with input validation
def format_name(fname, lname):
    if fname == "" or lname == "":
        return "You didn't provide valid inputs"
    formatted_fname = fname.title()
    formatted_lname = lname.title()
    return f"Result: {formatted_fname} {formatted_lname}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))


# Docstrings
def format_name(fname, lname):
    """Write anything"""
    formatted_fname = fname.title()
    formatted_lname = lname.title()
    return f"{formatted_fname} {formatted_lname}"

formatted_name = format_name("Abhi", "Pundit")
length = len(formatted_name)
print(formatted_name)
length=len("Abhi")
print(length)
