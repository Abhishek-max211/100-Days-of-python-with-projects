# Project-10 = The Calculator Project
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first Number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input("Type 'y' to continue calculating with previous answer, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n")
            calculator()

calculator()
