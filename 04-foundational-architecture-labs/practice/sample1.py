"""This module demonstrates a simple addition operation using a helper function."""
# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
def add(number1, number2):
    """The function returns the sum of 'number1' and 'number2'."""
    return number1 + number2

# Initialize the variable 'NUM1' with the value 4.
NUM1 = 4

# Initialize the variable 'NUM2' with the value 5.
NUM2 = 5

# Call the 'add' function with 'NUM1' and 'num2' as arguments and store the result in 'TOTAL'.
TOTAL = add(NUM1, NUM2)

# Print the result of adding 'NUM1' and 'NUM2'
# using an f-string to insert the
# values into the string instead of the format method.
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
