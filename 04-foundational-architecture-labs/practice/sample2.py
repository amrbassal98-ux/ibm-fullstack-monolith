"""This module demonstrates a simple Area calculator using a helper function."""
from math import pi

def area_calculator(shape, dimension1, dimension2=0):
    """This function returns the area of a rectangle or circle."""
    if shape == "rectangle":
        return dimension1 * dimension2
    if shape == "circle":
        # Calculate area using pi * r squared.
        r = dimension1
        # This is a very long comment explaining the formula for the area of a circle.
        return pi * pow(r, 2)
    return None

CURRENT_SHAPE = "rectangle"
VAL1 = 10
VAL2 = 5

RESULT = area_calculator(CURRENT_SHAPE, VAL1, VAL2)
print(RESULT)
