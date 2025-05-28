# Day 13
# Project-13 = Use of Debugger in Python
import pdb  # Python Debugger

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    # Intentional bug: wrong denominator (should be len(numbers))
    average = total / (len(numbers) + 1)

    return average

# Sample input
nums = [10, 20, 30, 40, 50]

# Insert a breakpoint before the function call
pdb.set_trace()

# Call the function
result = calculate_average(nums)
print("Average:", result)
